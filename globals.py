
def init():
    global now
    now = 0

    global severities

    # Descriptions of EMS Calls and their corresponding severities
    severities = {
        'CARDBR': 3,
        'INJMAJ': 1,
        'SICMIN': 2,
        'ASTHMB': 4,
        'DRUG': 1,
        'UNKNOW': 1,
        'SICK': 1,
        'UNC': 3,
        'INBLED': 2,
        'PEDSTR': 7,
        'EDP': 3,
        'INJMIN': 1,
        'SEIZR': 6,
        'INJURY': 6,
        'CVAC': 6,
        'ANAPH': 4,
        'EDPC': 3,
        'MVAINJ': 6,
        'ABDPN': 7,
        'SICPED': 6,
        'OTHER': 8,
        'RESPIR': 5,
        'CARD': 5,
        'DIFFBR': 1,
        'STAB': 2,
        'ALTMEN': 8,
        'CHOKE': 4,
        'STATEP': 1,
        'OBMIS': 3,
        'INHALE': 3,
        'ARREST': 5,
        'CVA': 4,
        'SHOT': 4,
        'PD13': 4,
        'BURNMA': 7,
        'STNDBY': 4,
        'OBMAJ': 1,
        'SAFE': 4,
        'OBLAB': 3,
        'MEDRXN': 7,
        'GYNMAJ': 3,
        'TRAUMA': 6,
        'GYNHEM': 4,
        'HYPTN': 3,
        'MCI21': 8,
        'COLD': 3,
        'JUMPUP': 2,
        'OBCOMP': 2,
        'BURNMI': 2,
        'CHILDA': 4,
        'STRANS': 8,
        'MVA': 6,
        'ELECT': 3,
        'JUMPDN': 5,
        'MCI77': 2,
        'VENOM': 2,
        'MVAINM': 2,
        'EDPW': 7,
        'ACTIVE': 2,
        'DROWN': 2,
        'OBOUT': 3,
        'AMPMIN': 4,
        'DIFFFC': 2,
        'MCI22': 2,
        'MOSILL': 9,
        'AMPMAJ': 3,
        'SPEVNT': 8,
        'SICKFC': 3,
        'HEAT': 4,
        'MOSINJ': 9,
        'MCI76': 2,
        'ASTHFC': 3,
        'RESPFC': 2,
        'PEDFC': 4,
        'STATFC': 2,
        'CARDFC': 3,
        'UNCFC': 2,
        'ABDPFC': 4,
        'MCI21P': 8,
        'SICKRF': 4,
        'FIRE77': 4,
        'RAPE': 4,
        'MCI43P': 2,
        'MCI22P': 2,
        'DOA': 7,
        'NOVEH': 9,
        'MCI29P': 2,
        'PEDRF': 4,
        'INBLFC': 3,
        'CVAFC': 4,
        'ALTMFC': 3,
        'MCI26P': 2,
        'DDOA': 9,
        'MCI34P': 2,
        'CVACFC': 2,
        'ACC': 6,
        'SEIZFC': 3,
        'DIFFRF': 2,
        'MCI50': 8,
        'MCI50P': 2,
        'MCI80P': 2,
        'INJALS': 4,
        'SICKFT': 3,
        'MCI32P': 2,
        'MCI44P': 2,
        'ASTHFT': 3,
        'STATFT': 2,
        'MCI25P': 2
    }
