import random

class BattleNarrativeGenerator:
    def __init__(self):
        self.narratives = {
            'melee': {
                'attack_verbs': {
                    'weak': [
                        "intenta un golpe rápido contra",
                        "lanza un puñetazo tentativo hacia",
                        "realiza un ataque cauteloso contra",
                        "ejecuta una finta ligera dirigida a",
                        "ensaya un movimiento de prueba contra",
                        "tantea las defensas de",
                        "busca una apertura en la guardia de",
                        "realiza un amago hacia",
                        "intenta un golpe de sondeo contra",
                        "lanza un ataque exploratorio hacia"
                    ],
                    'medium': [
                        "arremete con determinación contra",
                        "ejecuta una maniobra audaz dirigida a",
                        "lanza un ataque calculado hacia",
                        "descarga un golpe preciso contra",
                        "realiza una combinación de ataques hacia",
                        "ejecuta un movimiento fluido contra",
                        "despliega una técnica elaborada dirigida a",
                        "lanza una serie de golpes coordinados hacia",
                        "realiza un ataque con timing perfecto contra",
                        "desencadena una secuencia de movimientos contra"
                    ],
                    'strong': [
                        "desata un asalto devastador contra",
                        "ejecuta un golpe demoledor dirigido a",
                        "descarga toda su furia sobre",
                        "lanza un ataque con toda su fuerza contra",
                        "realiza un movimiento de una potencia descomunal hacia",
                        "canaliza toda su energía en un golpe brutal contra",
                        "desencadena un ataque de proporciones épicas sobre",
                        "ejecuta una técnica legendaria contra",
                        "descarga un golpe capaz de partir montañas sobre",
                        "lanza un ataque que hace temblar la tierra hacia"
                    ]
                },
                'impact_descriptions': {
                    'weak': [
                        "El golpe roza al objetivo, causando daño mínimo",
                        "El ataque conecta, pero carece de la fuerza necesaria para ser decisivo",
                        "El impacto es superficial, apenas perturbando al defensor",
                        "El golpe deja una marca leve, más molesta que dolorosa",
                        "El ataque logra poco más que irritar al oponente",
                        "El impacto es tan débil que apenas se nota",
                        "El golpe parece más un toque que un ataque real",
                        "El ataque apenas logra arañar la superficie de la defensa",
                        "El impacto es tan ligero que casi parece un accidente",
                        "El golpe conecta, pero sin la fuerza suficiente para causar preocupación"
                    ],
                    'medium': [
                        "El golpe conecta con precisión, causando un daño considerable",
                        "El ataque encuentra su objetivo, dejando una marca visible",
                        "El impacto resuena, señalando un golpe efectivo",
                        "El golpe penetra las defensas, causando dolor evidente",
                        "El ataque logra su cometido, debilitando al oponente",
                        "El impacto es sólido, haciendo retroceder al defensor",
                        "El golpe encuentra un punto vulnerable, maximizando su efecto",
                        "El ataque es ejecutado con maestría, logrando un daño significativo",
                        "El impacto sacude al defensor, dejándolo momentáneamente aturdido",
                        "El golpe es preciso y potente, cumpliendo su propósito a la perfección"
                    ],
                    'strong': [
                        "El impacto es devastador, sacudiendo todo el campo de batalla",
                        "El golpe crítico encuentra un punto débil, causando daño masivo",
                        "La fuerza del ataque es abrumadora, dejando al defensor tambaleándose",
                        "El impacto resuena con un estruendo ensordecedor, señalando su poder",
                        "El golpe parece desafiar las leyes de la física con su potencia",
                        "El ataque conecta con una fuerza capaz de derribar murallas",
                        "El impacto es tan poderoso que el aire alrededor se distorsiona",
                        "El golpe deja un rastro de destrucción en su camino hacia el objetivo",
                        "La potencia del ataque es tal que incluso los espectadores sienten su fuerza",
                        "El impacto es de una magnitud legendaria, digno de las historias épicas"
                    ]
                }
            },
            'ranged': {
                'attack_verbs': {
                    'weak': [
                        "dispara una flecha rápida hacia",
                        "lanza un proyectil ligero contra",
                        "realiza un disparo apresurado a",
                        "arroja un dardo pequeño en dirección a",
                        "dispara una bola de energía menor hacia",
                        "lanza una piedra con su honda contra",
                        "dispara un proyectil de baja potencia a",
                        "realiza un tiro de advertencia cerca de",
                        "lanza un bumerán ligero hacia",
                        "dispara una flecha de práctica contra"
                    ],
                    'medium': [
                        "apunta cuidadosamente y dispara a",
                        "lanza un proyectil con precisión hacia",
                        "ejecuta un tiro calculado contra",
                        "dispara una flecha con spin hacia",
                        "lanza un proyectil mágico dirigido a",
                        "realiza un disparo en curva hacia",
                        "ejecuta un tiro de rebote contra",
                        "lanza una jabalina con puntería perfecta a",
                        "dispara una ráfaga de proyectiles hacia",
                        "realiza un tiro de precisión apuntando a un punto débil de"
                    ],
                    'strong': [
                        "carga un proyectil devastador y lo dispara a",
                        "invoca una lluvia de proyectiles mortales sobre",
                        "desata un ataque a distancia de poder incomparable contra",
                        "dispara una flecha imbuida con energía ancestral hacia",
                        "lanza un proyectil capaz de atravesar montañas contra",
                        "canaliza el poder de los elementos en un disparo dirigido a",
                        "ejecuta un tiro legendario que busca aniquilar a",
                        "desata una tormenta de proyectiles devastadores sobre",
                        "dispara un rayo de energía pura concentrada hacia",
                        "lanza un proyectil que desafía las leyes de la física contra"
                    ]
                },
                'impact_descriptions': {
                    'weak': [
                        "El proyectil roza al objetivo, causando daño superficial",
                        "El tiro alcanza su marca, pero con impacto reducido",
                        "El ataque a distancia logra un efecto mínimo",
                        "El proyectil apenas rasguña la armadura del objetivo",
                        "El tiro conecta, pero sin la fuerza necesaria para ser efectivo",
                        "El impacto es tan leve que apenas distrae al objetivo",
                        "El proyectil rebota sin causar daño significativo",
                        "El tiro falla por poco, causando solo un susto momentáneo",
                        "El ataque a distancia es más molesto que dañino",
                        "El proyectil se desintegra al impactar, causando daño mínimo"
                    ],
                    'medium': [
                        "El proyectil encuentra su objetivo con precisión quirúrgica",
                        "El tiro conecta sólidamente, causando daño significativo",
                        "El ataque a distancia golpea un punto vulnerable",
                        "El proyectil penetra las defensas, logrando un impacto efectivo",
                        "El tiro alcanza su marca, dejando una herida visible",
                        "El impacto del proyectil hace retroceder al objetivo",
                        "El ataque a distancia encuentra un hueco en la armadura",
                        "El proyectil explota al impactar, maximizando el daño",
                        "El tiro preciso causa un daño considerable en el punto de impacto",
                        "El ataque logra su cometido, debilitando notablemente al objetivo"
                    ],
                    'strong': [
                        "El proyectil impacta con fuerza devastadora, sacudiendo al objetivo",
                        "El tiro perfecto causa un daño catastrófico",
                        "El ataque a distancia penetra todas las defensas con un poder abrumador",
                        "El proyectil atraviesa al objetivo, dejando un rastro de destrucción",
                        "El impacto del tiro resuena por todo el campo de batalla",
                        "El ataque a distancia desata una explosión de energía devastadora",
                        "El proyectil parece cobrar vida propia, buscando los puntos vitales",
                        "El tiro conecta con tal fuerza que distorsiona el aire a su alrededor",
                        "El ataque perfora incluso las defensas más sólidas como si fueran papel",
                        "El impacto del proyectil deja un cráter, evidenciando su poder destructivo"
                    ]
                }
            },
            'magic': {
                'attack_verbs': {
                    'weak': [
                        "lanza un hechizo menor contra",
                        "invoca una chispa mágica dirigida a",
                        "canaliza una corriente de energía arcana hacia",
                        "murmura un encantamiento básico contra",
                        "dibuja un sello mágico simple frente a",
                        "proyecta un destello de luz mágica hacia",
                        "convoca una brisa arcana que sopla hacia",
                        "crea una ilusión menor para confundir a",
                        "lanza un dardo mágico de baja potencia a",
                        "genera un pulso de energía débil dirigido a"
                    ],
                    'medium': [
                        "conjura un poderoso encantamiento contra",
                        "desata fuerzas arcanas sobre",
                        "teje un complejo patrón de energía mágica alrededor de",
                        "invoca los elementos para castigar a",
                        "canaliza las energías del plano astral hacia",
                        "recita un antiguo conjuro dirigido a",
                        "manipula las corrientes mágicas para atacar a",
                        "desencadena un vórtice de poder arcano sobre",
                        "convoca espíritus elementales para arremeter contra",
                        "fusiona diferentes escuelas de magia en un ataque contra"
                    ],
                    'strong': [
                        "invoca poderes cósmicos para aniquilar a",
                        "desencadena un cataclismo mágico sobre",
                        "abre un portal a dimensiones de pesadilla para consumir a",
                        "canaliza la furia de dioses antiguos contra",
                        "desata una tormenta de energía primordial sobre",
                        "invoca la ira de la naturaleza misma contra",
                        "rasga el tejido de la realidad para atacar a",
                        "convoca fuerzas más allá de la comprensión mortal para destruir a",
                        "desencadena un maremoto de poder arcano contra",
                        "fusiona su esencia con la magia pura para aniquilar a"
                    ]
                },
                'impact_descriptions': {
                    'weak': [
                        "El hechizo causa un leve cosquilleo mágico",
                        "La energía arcana roza al objetivo, causando daño mínimo",
                        "El ataque mágico logra un efecto casi imperceptible",
                        "El hechizo crea una breve distorsión en el aire, apenas afectando al objetivo",
                        "La magia menor causa un destello inofensivo al impactar",
                        "El conjuro débil apenas logra irritar al objetivo",
                        "La energía mágica se disipa rápidamente, causando poco efecto",
                        "El hechizo crea una ilusión molesta pero inofensiva",
                        "El ataque arcano menor causa un leve mareo en el objetivo",
                        "La magia de bajo nivel apenas logra llamar la atención del defensor"
                    ],
                    'medium': [
                        "El hechizo envuelve al objetivo en una vorágine de energía",
                        "Las fuerzas mágicas sacuden la realidad alrededor del defensor",
                        "El impacto arcano resuena con un eco sobrenatural",
                        "El conjuro manipula los elementos, causando daño significativo",
                        "La magia distorsiona el espacio alrededor del objetivo, desorientándolo",
                        "El ataque mágico crea una explosión de energía pura",
                        "El hechizo invoca fuerzas elementales que castigan al defensor",
                        "La energía arcana penetra las defensas, causando daño interno",
                        "El conjuro crea una zona de caos mágico alrededor del objetivo",
                        "La magia altera temporalmente la realidad, afectando gravemente al defensor"
                    ],
                    'strong': [
                        "El hechizo desata un cataclismo de energía pura sobre el objetivo",
                        "Las fuerzas arcanas invocadas doblan el tejido de la realidad",
                        "El ataque mágico consume al defensor en un vórtice de poder primordial",
                        "El conjuro abre brevemente un portal al caos, devastando al objetivo",
                        "La magia desatada causa una implosión de energía cósmica",
                        "El hechizo invoca el poder de estrellas moribundas contra el defensor",
                        "Las fuerzas mágicas desencadenadas amenazan con desgarrar la realidad misma",
                        "El ataque arcano fusiona momentáneamente al objetivo con el plano elemental",
                        "El conjuro supremo manifiesta horrores de otros planos contra el defensor",
                        "La magia pura en su forma más destructiva se materializa, aniquilando todo a su paso"
                    ]
                }
            },
            'defense_verbs': {
                'successful': [
                    "logra esquivar ágilmente",
                    "bloquea con maestría",
                    "anticipa y evita",
                    "desvía hábilmente",
                    "contrarresta con precisión",
                    "neutraliza eficazmente",
                                        "se protege, aunque no de manera perfecta",
                    "anticipa el ataque, pero no logra evadirlo completamente",
                    "intenta una defensa que resulta solo parcialmente efectiva",
                    "logra reducir el impacto, pero aún sufre daño"
                ],
                'failed': [
                    "no logra reaccionar a tiempo ante",
                    "es tomado por sorpresa por",
                    "falla en su intento de defenderse de",
                    "queda expuesto ante",
                    "es superado por la velocidad de",
                    "no consigue anticipar",
                    "es abrumado por la fuerza de",
                    "subestima la potencia de",
                    "cae en la trampa tendida por",
                    "es incapaz de contrarrestar"
                ]
            },
            'environment_effects': {
                'neutral': [
                    "El viento sopla suavemente, llevando el eco del combate",
                    "El sol brilla en lo alto, iluminando el campo de batalla",
                    "Una calma tensa envuelve el área, como la quietud antes de la tormenta",
                    "Las nubes se desplazan lentamente en el cielo, ajenas al conflicto",
                    "Un silencio sepulcral cae sobre el campo, roto solo por el choque de armas",
                    "El aire está cargado de expectación, como si la naturaleza contuviera el aliento",
                    "Una brisa fresca recorre el campo de batalla, ofreciendo un breve respiro",
                    "El terreno permanece firme bajo los pies de los combatientes",
                    "Los sonidos de la naturaleza continúan, indiferentes a la batalla",
                    "La luz del día se mantiene constante, sin favorecer a ningún bando"
                ],
                'advantageous': [
                    "Un terreno elevado proporciona ventaja estratégica",
                    "Las sombras del entorno ofrecen oportunidades para ataques sorpresa",
                    "Una corriente de energía mágica potencia los hechizos lanzados",
                    "Rocas y escombros proporcionan cobertura natural",
                    "Un viento favorable aumenta el alcance de los proyectiles",
                    "La vegetación densa ofrece puntos de emboscada",
                    "Corrientes de agua subterráneas revitalizan a los combatientes",
                    "Formaciones rocosas naturales actúan como barreras defensivas",
                    "Un campo de energía residual amplifica los ataques mágicos",
                    "La configuración del terreno canaliza los ataques, aumentando su efectividad"
                ],
                'disadvantageous': [
                    "El suelo inestable dificulta mantener el equilibrio",
                    "Una densa niebla reduce la visibilidad, complicando los ataques a distancia",
                    "Fuertes vientos desvían los proyectiles de su curso",
                    "La lluvia torrencial hace que el terreno sea resbaladizo",
                    "El calor abrasador agota rápidamente a los combatientes",
                    "Relámpagos aleatorios amenazan con golpear en cualquier momento",
                    "Grietas en el suelo emanan gases venenosos",
                    "La vegetación espesa entorpece los movimientos",
                    "Un campo de fuerza natural interfiere con la magia",
                    "Temblores repentinos desestabilizan a los luchadores"
                ]
            },
            'emotions': {
                'intense': [
                    "La determinación brilla en los ojos de {attacker}, mientras {defender} muestra una resolución inquebrantable",
                    "La tensión en el aire es tan densa que podría cortarse con un cuchillo",
                    "Ambos combatientes emanan un aura de poder que hace temblar el aire a su alrededor",
                    "El choque de voluntades entre {attacker} y {defender} parece hacer temblar los cimientos de la realidad",
                    "Una energía electrizante recorre el campo de batalla, emanando de los dos guerreros",
                    "Los ojos de {attacker} arden con una intensidad sobrenatural, reflejada en la mirada de {defender}",
                    "El aire crepita con la tensión acumulada entre los dos titanes enfrentados",
                    "Una sensación de destino inevitable envuelve a {attacker} y {defender}, como si su enfrentamiento estuviera escrito en las estrellas",
                    "La ferocidad de la batalla alcanza nuevas cotas, llevando a ambos combatientes al límite",
                    "Un silencio sobrenatural cae sobre el campo, roto solo por el choque de voluntades entre {attacker} y {defender}"
                ],
                'strategic': [
                    "{attacker} estudia cada movimiento de {defender}, buscando una apertura",
                    "Un duelo de voluntades se desarrolla, cada luchador anticipando el próximo movimiento del otro",
                    "La concentración de ambos es tan intensa que el mundo alrededor parece desvanecerse",
                    "{defender} analiza meticulosamente la postura de {attacker}, preparándose para cualquier eventualidad",
                    "Ambos guerreros se mueven en círculos, evaluando las fortalezas y debilidades del otro",
                    "Un juego de ajedrez mortal se desarrolla entre {attacker} y {defender}, cada movimiento cuidadosamente calculado",
                    "La tensión estratégica es palpable, con ambos combatientes esperando el momento perfecto para atacar",
                    "{attacker} y {defender} intercambian miradas cargadas de cálculo, cada uno tratando de descifrar la estrategia del otro",
                    "Un baile mortal de fintas y contra-fintas se desarrolla entre los dos guerreros",
                    "La batalla se convierte en un duelo de mentes tanto como de cuerpos, con cada acción meticulosamente planeada"
                ],
                'desperate': [
                    "La desesperación comienza a reflejarse en los ojos de {defender} ante el implacable asalto",
                    "{attacker} presiona su ventaja con ferocidad, sintiendo la victoria al alcance",
                    "El aire se carga con la energía del último esfuerzo de ambos combatientes",
                    "{defender} lucha con una determinación nacida de la desesperación, negándose a ceder",
                    "Un frenesí de ataques y contraataques se desata, con ambos luchadores dándolo todo",
                    "La batalla alcanza un punto crítico, con {attacker} y {defender} al borde de sus límites",
                    "El campo de batalla se llena de una energía caótica, reflejando la desesperación de la lucha",
                    "{attacker} ataca con una urgencia renovada, consciente de que el final está cerca",
                    "Los movimientos de {defender} se vuelven más erráticos, impulsados por una mezcla de miedo y determinación",
                    "Un grito de batalla resuena, cargado con la emoción cruda de un combate que llega a su clímax"
                ]
            }
        }

    def generate_narrative(self, attacker_action, defender_action, damage, environment, emotional_state):
        attacker = attacker_action.name
        defender = defender_action.name
        attack_type = attacker_action.attack.type if attacker_action.attack else 'melee'
        attack_strength = self._get_attack_strength(attacker_action.attack_strength)
        defense_success = 'successful' if defender_action.defense_success else 'failed'

        narrative = []

        # Descripción del entorno
        narrative.append(random.choice(self.narratives['environment_effects'][environment.effect_type]))

        # Acción del atacante
        attack_description = f"{attacker} {random.choice(self.narratives[attack_type]['attack_verbs'][attack_strength])} {defender}. "
        narrative.append(attack_description)

        # Reacción del defensor
        defense_description = f"{defender} {random.choice(self.narratives['defense_verbs'][defense_success])} el ataque. "
        narrative.append(defense_description)

        # Resultado del ataque
        if damage > 0:
            if attacker_action.attack_strength > attacker_action.attack.base_damage:
                narrative.append("¡Golpe crítico! " + random.choice(self.narratives[attack_type]['impact_descriptions']['strong']))
            else:
                narrative.append(random.choice(self.narratives[attack_type]['impact_descriptions'][attack_strength]))
            
            damage_description = f"{defender} sufre {damage} puntos de daño"
            if defender_action.hp > 0:
                damage_description += f" y queda con {defender_action.hp} puntos de vida restantes."
            else:
                damage_description += f" y cae derrotado, su valentía grabada para siempre en los anales de la historia."
            narrative.append(damage_description)
        else:
            narrative.append(f"El ataque falla completamente. {defender} mantiene sus {defender_action.hp} puntos de vida intactos.")

        # Añadir una descripción de la reacción emocional o la atmósfera
        emotion = random.choice(self.narratives['emotions'][self._get_emotional_intensity(emotional_state)]).format(attacker=attacker, defender=defender)
        narrative.append(emotion)

        return " ".join(narrative)

    def _get_attack_strength(self, attack_strength):
        if attack_strength <= 3:
            return 'weak'
        elif attack_strength <= 6:
            return 'medium'
        else:
            return 'strong'

    def _get_emotional_intensity(self, emotional_state):
        emotions = list(emotional_state.values())
        if 'eufórico' in emotions or 'asustado' in emotions:
            return 'intense'
        elif 'concentrado' in emotions or 'cauteloso' in emotions:
            return 'strategic'
        else:
            return 'desperate'
