import random
from typing import List, Dict, Optional, Tuple
from services.battle_narrative_generator import BattleNarrativeGenerator
from dataclass import CharacterAction, CharacterInfo, Round, BattleResult
from models.character import Character
from models.environment import Environment
from models.item import Attack
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class BattleCharacter:
    def __init__(self, character: Character, environment: Environment):
        self.character = character
        self.environment = environment
        self.modifiers = environment.get_modifiers()

    @property
    def strength(self):
        base_strength = self.character.strength  # Ya incluye los bonos de los items
        return int(base_strength * self.modifiers['attack'])

    @property
    def defense(self):
        base_defense = self.character.defense  # Ya incluye los bonos de los items
        return int(base_defense * self.modifiers['defense'])

    @property
    def agility(self):
        return self.character.agility  # Asumimos que el entorno no afecta la agilidad

    @property
    def dodge_chance(self):
        base_dodge = self.character.dodge_chance
        item_dodge_bonus = sum(item.dodge_bonus for item in self.character.equipped_items)
        return (base_dodge + item_dodge_bonus) * self.modifiers['dodge']

    @property
    def critical_chance(self):
        base_critical = self.character.critical_chance
        item_critical_bonus = sum(item.critical_chance_bonus for item in self.character.equipped_items)
        return base_critical + item_critical_bonus  # Asumimos que el entorno no afecta la probabilidad crítica

    @property
    def health(self):
        return self.character.health

    @property
    def max_health(self):
        return self.character.max_health

    @property
    def mana(self):
        return self.character.mana

    @property
    def max_mana(self):
        return self.character.max_mana

    @property
    def name(self):
        return self.character.name

    @property
    def image(self):
        return self.character.image

    @property
    def character_items(self):
        return self.character.items

    def get_available_attacks(self):
        return self.character.get_available_attacks()

    def __getattr__(self, name):
        return getattr(self.character, name)

class BattleService:
    def __init__(self, character1: Character, character2: Character, environment: Environment):
        self.battle_character1 = BattleCharacter(character1, environment)
        self.battle_character2 = BattleCharacter(character2, environment)
        self.environment = environment

    def conduct_battle(self) -> BattleResult:
        character1_hp, character2_hp = self.battle_character1.health, self.battle_character2.health
        rounds: List[Round] = []
        emotional_state = self._generate_initial_emotional_state(self.battle_character1, self.battle_character2)
        
        while character1_hp > 0 and character2_hp > 0:
            character1_hp, character2_hp, rounds, emotional_state = self._process_round(
                self.battle_character1, self.battle_character2, character1_hp, character2_hp, rounds, emotional_state)

        winner = self.battle_character1.name if character1_hp > 0 else self.battle_character2.name
        return self._create_battle_result(self.battle_character1, self.battle_character2, character1_hp, character2_hp, rounds, winner)

    def _process_round(self, character1: BattleCharacter, character2: BattleCharacter, character1_hp: int, character2_hp: int, 
                       rounds: List[Round], emotional_state: Dict[str, str]) -> Tuple[int, int, List[Round], Dict[str, str]]:
        round_number = len(rounds) + 1
        round_data = self._process_attack(round_number, character1, character2, character1_hp, character2_hp, emotional_state)
        rounds.append(round_data)
        character1_hp, character2_hp = round_data.character1.hp, round_data.character2.hp
        emotional_state = self._update_emotional_state(emotional_state, round_data)

        if character2_hp > 0:
            round_data = self._process_attack(round_number, character2, character1, character2_hp, character1_hp, emotional_state)
            rounds.append(round_data)
            character1_hp, character2_hp = round_data.character1.hp, round_data.character2.hp
            emotional_state = self._update_emotional_state(emotional_state, round_data)

        return character1_hp, character2_hp, rounds, emotional_state

    def _create_battle_result(self, character1: BattleCharacter, character2: BattleCharacter, character1_hp: int, character2_hp: int, 
                              rounds: List[Round], winner: str) -> BattleResult:
        return BattleResult(
            character1=self._create_character_info(character1, character1_hp),
            character2=self._create_character_info(character2, character2_hp),
            rounds=rounds,
            winner=winner
        )

    def _process_attack(self, round_number: int, attacker: BattleCharacter, defender: BattleCharacter, attacker_hp: int, defender_hp: int, 
                        emotional_state: Dict[str, str]) -> Round:
        attack = self._select_attack(attacker)
        attack_strength, attack_action = self._calculate_attack_strength(attacker, attack)
        damage, defense_action = self._calculate_defense(defender, attack_strength)
        new_defender_hp = max(defender_hp - damage, 0)

        attacker_action = self._create_character_action(attacker, attack_action, attacker_hp, attack, attack_strength)
        defender_action = self._create_character_action(defender, defense_action, new_defender_hp, defense_success=(damage == 0))

        return self._create_round(round_number, attacker, defender, attacker_action, defender_action, damage, emotional_state)

    def _calculate_attack_strength(self, attacker: BattleCharacter, attack: Attack) -> Tuple[int, str]:
        if random.random() < attacker.critical_chance:
            attack_strength = int(attack.base_damage * attack.critical_multiplier)
            attack_action = "¡golpe crítico!"
        else:
            attack_strength = attack.base_damage
            attack_action = f"usa {attack.name}"

        attack_item = next((item for item in attacker.character_items if item.base_item.id == attack.item_id), None)
        if attack_item and attack_item.aura:
            attack_strength = int(attack_strength * attack_item.aura.multiplier)

        return attack_strength, attack_action

    def _calculate_defense(self, defender: BattleCharacter, attack_strength: int) -> Tuple[int, str]:
        if random.random() < defender.dodge_chance:
            return 0, "¡esquiva completamente el ataque!"
        else:
            damage = max(attack_strength - defender.defense, 1)
            return damage, "recibe"

    def _create_character_action(self, character: BattleCharacter, action: str, hp: int, attack: Optional[Attack] = None, 
                                 attack_strength: Optional[int] = None, defense_success: Optional[bool] = None) -> CharacterAction:
        return CharacterAction(
            name=character.name,
            action=action,
            initial_hp=character.health,
            hp=hp,
            is_attacker=(attack is not None),
            attack=attack,
            attack_strength=attack_strength,
            defense_success=defense_success,
            available_attacks=self.get_available_attacks(character),
            available_items=character.character_items
        )

    def _create_round(self, round_number: int, attacker: BattleCharacter, defender: BattleCharacter, attacker_action: CharacterAction, 
                      defender_action: CharacterAction, damage: int, emotional_state: Dict[str, str]) -> Round:
        character1 = attacker_action if attacker.character.id == self.battle_character1.character.id else defender_action
        character2 = defender_action if attacker.character.id == self.battle_character1.character.id else attacker_action
        narrative = BattleNarrativeGenerator().generate_narrative(
            attacker_action, defender_action, damage, self.environment, emotional_state
        )

        return Round(
            number=round_number,
            character1=character1,
            character2=character2,
            damage=damage,
            narrative=narrative,
            environment=self.environment,
            emotional_state=emotional_state
        )

    def _create_character_info(self, character: BattleCharacter, final_hp: int) -> CharacterInfo:
        return CharacterInfo(
            name=character.name,
            image=character.image.url,
            strength=character.strength,
            defense=character.defense,
            agility=character.agility,
            health=character.health,
            max_health=character.max_health,
            mana=character.mana,
            max_mana=character.max_mana,
            critical_chance=character.critical_chance,
            dodge_chance=character.dodge_chance,
            initial_hp=character.health,
            final_hp=max(final_hp, 0),
            items=character.character_items,
            attacks=self.get_available_attacks(character)
        )

    def _select_attack(self, character: BattleCharacter) -> Optional[Attack]:
        available_attacks = self.get_available_attacks(character)
        return random.choice(available_attacks) if available_attacks else None

    def get_available_attacks(self, character: BattleCharacter) -> List[Attack]:
        available_attacks: List[Attack] = []
        for character_item in character.character_items:
            if character_item.equipped:
                available_attacks.extend(character_item.base_item.attacks)
        return available_attacks

    def _generate_initial_emotional_state(self, character1: BattleCharacter, character2: BattleCharacter) -> Dict[str, str]:
        return {
            character1.name: "determinado",
            character2.name: "determinado"
        }

    def _update_emotional_state(self, current_state: Dict[str, str], round_data: Round) -> Dict[str, str]:
        new_state = current_state.copy()

        for character in [round_data.character1, round_data.character2]:
            if character.is_attacker:
                if character.attack_strength > character.attack.base_damage:
                    new_state[character.name] = "eufórico"
                elif round_data.damage == 0:
                    new_state[character.name] = "frustrado"
                else:
                    new_state[character.name] = "concentrado"
            else:
                if character.defense_success:
                    new_state[character.name] = "confiado"
                elif round_data.damage > 5:  # Usamos un valor arbitrario para daño alto
                    new_state[character.name] = "asustado"
                else:
                    new_state[character.name] = "cauteloso"
        
        return new_state