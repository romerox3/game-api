from dataclasses import dataclass, field
from typing import List, Dict, Optional
from models.environment import Environment
from models.item import Attack, Item

@dataclass
class CharacterAction:
    name: str
    action: str
    initial_hp: int
    hp: int
    is_attacker: bool
    attack: Optional[Attack] = None
    attack_strength: Optional[int] = None
    defense_success: Optional[bool] = None
    available_attacks: List[Attack] = field(default_factory=list)
    available_items: List[Item] = field(default_factory=list)

@dataclass
class CharacterInfo:
    name: str
    image: str
    initial_hp: int
    final_hp: int
    strength: int
    defense: int
    agility: int
    health: int
    max_health: int
    mana: int
    max_mana: int
    critical_chance: float
    dodge_chance: float 
    attacks: List[Attack]
    items: List[Item]

@dataclass
class Round:
    number: int
    character1: CharacterAction
    character2: CharacterAction
    damage: int
    narrative: str
    environment: Environment
    emotional_state: Dict[str, str]

@dataclass
class BattleResult:
    character1: CharacterInfo
    character2: CharacterInfo
    rounds: List[Round]
    winner: str