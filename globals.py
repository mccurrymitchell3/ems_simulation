
import datetime


def init():
    global now
    now = 0

    global severities

    # Descriptions of EMS Calls and their corresponding severities
    severities = {'CARDBR': 2,
                  'INJURY': 5,
                  'SEIZR': 3,
                  'MVAINJ': 4,
                  'EDP': 7,
                  'PEDSTR': 3,
                  'UNKNOW': 4,
                  'DRUG': 4,
                  'TRAUMA': 2,
                  'SICK': 6,
                  'SICPED': 4,
                  'OBLAB': 5,
                  'INJMIN': 7,
                  'INJMAJ': 3,
                  'DIFFBR': 2,
                  'CARD': 3,
                  'ASTHMB': 2,
                  'SICMIN': 7,
                  'EDPC': 5,
                  'UNC': 2,
                  'OTHER': 6,
                  'STATEP': 2,
                  'SHOT': 3,
                  'ALTMEN': 3,
                  'ARREST': 1,
                  'GYNHEM': 5,
                  'SAFE': 6,
                  'CVAC': 2,
                  'ABDPN': 5,
                  'INHALE': 5,
                  'INBLED': 3,
                  'RESPIR': 4,
                  'STAB': 3,
                  'HYPTN': 7,
                  'CVA': 4,
                  'MEDRXN': 5,
                  'COLD': 5,
                  'ANAPH': 2,
                  'OBMAJ': 3,
                  'BURNMI': 7,
                  'JUMPDN': 2,
                  'CHOKE': 1,
                  'PD13': 7,
                  'OBMIS': 4,
                  'GYNMAJ': 3,
                  'STNDBY': 8,
                  'OBOUT': 3,
                  'ACTIVE': 2,
                  'MCI21': 2,
                  'OBCOMP': 2,
                  'BURNMA': 3,
                  'STRANS': 8,
                  'AMPMIN': 5,
                  'DROWN': 2,
                  'HEAT': 4,
                  'MVA': 6,
                  'CHILDA': 6,
                  'ELECT': 3,
                  'JUMPUP': 7,
                  'SICKFC': 6,
                  'MCI77': 2,
                  'PD13C': 3,
                  'AMPMAJ': 3,
                  'DIFFFC': 2,
                  'PEDFC': 4,
                  'SPEVNT': 8,
                  'MEDVAC': 2,
                  'CARDFC': 3,
                  'ABDPFC': 5,
                  'RESPFC': 4,
                  'ASTHFC': 2,
                  'MEDRFC': 5,
                  'PEDRF': 4,
                  'VENOM': 2,
                  'MCI21P': 2,
                  'SICKRF': 6,
                  'RAPE': 6,
                  'MCI43P': 2,
                  'CVAFC': 4,
                  'CVACFC': 2,
                  'INBLFC': 3,
                  'ALTMFC': 3,
                  'DIFFRF': 2,
                  'SEIZFC': 3,
                  'MCI26P': 2,
                  'STATFC': 2,
                  'MCI29P': 2,
                  'INJALS': 3,
                  'MCI22P': 2,
                  'DRUGFC': 4,
                  'SICKFT': 3}

    global severity_proportions
    severity_proportions = {2: 0.2305695144215619,
                            5: 0.17751217547007442,
                            3: 0.13628264491935052,
                            4: 0.16728339142317555,
                            6: 0.16517475574117008,
                            7: 0.10258176264102964,
                            1: 0.019097629685846915,
                            8: 0.0014981256977909775}


    global severity_weights_list
    severity_weights_list = [0.019097629685846915, 0.2305695144215619, 0.13628264491935052,
                            0.16728339142317555, 0.17751217547007442, 0.16517475574117008, 0.10258176264102964,
                            0.0014981256977909775]

    # # grouped incident descriptions from 1 - 8
    # global severity_list
    # severity_list = [['ARREST', 'CHOKE'], ['CARDBR', 'TRAUMA', 'DIFFBR', 'ASTHMB', 'UNC', 'STATEP', 'CVAC', 'ANAPH', 'JUMPDN', 'ACTIVE', 'MCI21', 'OBCOMP', 'DROWN', 'MCI77', 'DIFFFC', 'MEDVAC', 'ASTHFC', 'VENOM', 'MCI21P', 'MCI43P', 'CVACFC', 'DIFFRF', 'MCI26P', 'STATFC', 'MCI29P', 'MCI22P'], ['SEIZR', 'PEDSTR', 'INJMAJ', 'CARD', 'SHOT', 'ALTMEN', 'INBLED', 'STAB', 'OBMAJ', 'GYNMAJ', 'OBOUT', 'BURNMA', 'ELECT', 'PD13C', 'AMPMAJ', 'CARDFC',
    #                                                                                                                                                                                                                                                                                                 'INBLFC', 'ALTMFC', 'SEIZFC', 'INJALS', 'SICKFT'], ['MVAINJ', 'UNKNOW', 'DRUG', 'SICPED', 'RESPIR', 'CVA', 'OBMIS', 'HEAT', 'PEDFC', 'RESPFC', 'PEDRF', 'CVAFC', 'DRUGFC'], ['INJURY', 'OBLAB', 'EDPC', 'GYNHEM', 'ABDPN', 'INHALE', 'MEDRXN', 'COLD', 'AMPMIN', 'ABDPFC', 'MEDRFC'], ['SICK', 'OTHER', 'SAFE', 'MVA', 'CHILDA', 'SICKFC', 'SICKRF', 'RAPE'], ['EDP', 'INJMIN', 'SICMIN', 'HYPTN', 'BURNMI', 'PD13', 'JUMPUP'], ['STNDBY', 'STRANS', 'SPEVNT']]

    global severity_to_description
    severity_to_description = {1: ['ARREST', 'CHOKE'], 2: ['CARDBR', 'TRAUMA', 'DIFFBR', 'ASTHMB', 'UNC', 'STATEP', 'CVAC', 'ANAPH', 'JUMPDN', 'ACTIVE', 'MCI21', 'OBCOMP', 'DROWN', 'MCI77', 'DIFFFC', 'MEDVAC', 'ASTHFC', 'VENOM', 'MCI21P', 'MCI43P', 'CVACFC', 'DIFFRF', 'MCI26P', 'STATFC', 'MCI29P', 'MCI22P'], 3: ['SEIZR', 'PEDSTR', 'INJMAJ', 'CARD', 'SHOT', 'ALTMEN', 'INBLED', 'STAB', 'OBMAJ', 'GYNMAJ', 'OBOUT', 'BURNMA', 'ELECT', 'PD13C', 'AMPMAJ', 'CARDFC',
                                                                                                                                                                                                                                                                                                                          'INBLFC', 'ALTMFC', 'SEIZFC', 'INJALS', 'SICKFT'], 4: ['MVAINJ', 'UNKNOW', 'DRUG', 'SICPED', 'RESPIR', 'CVA', 'OBMIS', 'HEAT', 'PEDFC', 'RESPFC', 'PEDRF', 'CVAFC', 'DRUGFC'], 5: ['INJURY', 'OBLAB', 'EDPC', 'GYNHEM', 'ABDPN', 'INHALE', 'MEDRXN', 'COLD', 'AMPMIN', 'ABDPFC', 'MEDRFC'], 6: ['SICK', 'OTHER', 'SAFE', 'MVA', 'CHILDA', 'SICKFC', 'SICKRF', 'RAPE'], 7: ['EDP', 'INJMIN', 'SICMIN', 'HYPTN', 'BURNMI', 'PD13', 'JUMPUP'], 8: ['STNDBY', 'STRANS', 'SPEVNT']}

    global callfreq_by_time
    callfreq_weekdays = {datetime.time(0, 0): 9,
                      datetime.time(0, 15): 8,
                      datetime.time(0, 30): 8,
                      datetime.time(0, 45): 8,
                      datetime.time(1, 0): 7,
                      datetime.time(1, 15): 7,
                      datetime.time(1, 30): 7,
                      datetime.time(1, 45): 7,
                      datetime.time(2, 0): 6,
                      datetime.time(2, 15): 6,
                      datetime.time(2, 30): 6,
                      datetime.time(2, 45): 6,
                      datetime.time(3, 0): 5,
                      datetime.time(3, 15): 5,
                      datetime.time(3, 30): 5,
                      datetime.time(3, 45): 5,
                      datetime.time(4, 0): 5,
                      datetime.time(4, 15): 5,
                      datetime.time(4, 30): 5,
                      datetime.time(4, 45): 5,
                      datetime.time(5, 0): 5,
                      datetime.time(5, 15): 5,
                      datetime.time(5, 30): 5,
                      datetime.time(5, 45): 5,
                      datetime.time(6, 0): 5,
                      datetime.time(6, 15): 5,
                      datetime.time(6, 30): 5,
                      datetime.time(6, 45): 5,
                      datetime.time(7, 0): 6,
                      datetime.time(7, 15): 7,
                      datetime.time(7, 30): 7,
                      datetime.time(7, 45): 8,
                      datetime.time(8, 0): 8,
                      datetime.time(8, 15): 9,
                      datetime.time(8, 30): 10,
                      datetime.time(8, 45): 10,
                      datetime.time(9, 0): 11,
                      datetime.time(9, 15): 12,
                      datetime.time(9, 30): 12,
                      datetime.time(9, 45): 12,
                      datetime.time(10, 0): 12,
                      datetime.time(10, 15): 13,
                      datetime.time(10, 30): 13,
                      datetime.time(10, 45): 13,
                      datetime.time(11, 0): 13,
                      datetime.time(11, 15): 13,
                      datetime.time(11, 30): 13,
                      datetime.time(11, 45): 13,
                      datetime.time(12, 0): 13,
                      datetime.time(12, 15): 13,
                      datetime.time(12, 30): 13,
                      datetime.time(12, 45): 13,
                      datetime.time(13, 0): 13,
                      datetime.time(13, 15): 13,
                      datetime.time(13, 30): 13,
                      datetime.time(13, 45): 13,
                      datetime.time(14, 0): 13,
                      datetime.time(14, 15): 13,
                      datetime.time(14, 30): 13,
                      datetime.time(14, 45): 13,
                      datetime.time(15, 0): 13,
                      datetime.time(15, 15): 13,
                      datetime.time(15, 30): 13,
                      datetime.time(15, 45): 13,
                      datetime.time(16, 0): 12,
                      datetime.time(16, 15): 13,
                      datetime.time(16, 30): 12,
                      datetime.time(16, 45): 13,
                      datetime.time(17, 0): 13,
                      datetime.time(17, 15): 12,
                      datetime.time(17, 30): 12,
                      datetime.time(17, 45): 12,
                      datetime.time(18, 0): 12,
                      datetime.time(18, 15): 12,
                      datetime.time(18, 30): 12,
                      datetime.time(18, 45): 12,
                      datetime.time(19, 0): 12,
                      datetime.time(19, 15): 12,
                      datetime.time(19, 30): 12,
                      datetime.time(19, 45): 12,
                      datetime.time(20, 0): 12,
                      datetime.time(20, 15): 12,
                      datetime.time(20, 30): 12,
                      datetime.time(20, 45): 11,
                      datetime.time(21, 0): 12,
                      datetime.time(21, 15): 11,
                      datetime.time(21, 30): 11,
                      datetime.time(21, 45): 11,
                      datetime.time(22, 0): 11,
                      datetime.time(22, 15): 11,
                      datetime.time(22, 30): 11,
                      datetime.time(22, 45): 10,
                      datetime.time(23, 0): 10,
                      datetime.time(23, 15): 10,
                      datetime.time(23, 30): 9,
                      datetime.time(23, 45): 9}

    callfreq_weekends = {datetime.time(0, 0): 10,
                      datetime.time(0, 15): 10,
                      datetime.time(0, 30): 10,
                      datetime.time(0, 45): 9,
                      datetime.time(1, 0): 9,
                      datetime.time(1, 15): 9,
                      datetime.time(1, 30): 9,
                      datetime.time(1, 45): 8,
                      datetime.time(2, 0): 8,
                      datetime.time(2, 15): 8,
                      datetime.time(2, 30): 8,
                      datetime.time(2, 45): 8,
                      datetime.time(3, 0): 7,
                      datetime.time(3, 15): 7,
                      datetime.time(3, 30): 7,
                      datetime.time(3, 45): 7,
                      datetime.time(4, 0): 7,
                      datetime.time(4, 15): 7,
                      datetime.time(4, 30): 7,
                      datetime.time(4, 45): 7,
                      datetime.time(5, 0): 6,
                      datetime.time(5, 15): 6,
                      datetime.time(5, 30): 6,
                      datetime.time(5, 45): 6,
                      datetime.time(6, 0): 6,
                      datetime.time(6, 15): 6,
                      datetime.time(6, 30): 6,
                      datetime.time(6, 45): 5,
                      datetime.time(7, 0): 6,
                      datetime.time(7, 15): 6,
                      datetime.time(7, 30): 6,
                      datetime.time(7, 45): 6,
                      datetime.time(8, 0): 6,
                      datetime.time(8, 15): 7,
                      datetime.time(8, 30): 7,
                      datetime.time(8, 45): 7,
                      datetime.time(9, 0): 8,
                      datetime.time(9, 15): 8,
                      datetime.time(9, 30): 9,
                      datetime.time(9, 45): 9,
                      datetime.time(10, 0): 9,
                      datetime.time(10, 15): 9,
                      datetime.time(10, 30): 10,
                      datetime.time(10, 45): 10,
                      datetime.time(11, 0): 10,
                      datetime.time(11, 15): 10,
                      datetime.time(11, 30): 10,
                      datetime.time(11, 45): 10,
                      datetime.time(12, 0): 10,
                      datetime.time(12, 15): 11,
                      datetime.time(12, 30): 11,
                      datetime.time(12, 45): 11,
                      datetime.time(13, 0): 11,
                      datetime.time(13, 15): 11,
                      datetime.time(13, 30): 11,
                      datetime.time(13, 45): 11,
                      datetime.time(14, 0): 11,
                      datetime.time(14, 15): 11,
                      datetime.time(14, 30): 11,
                      datetime.time(14, 45): 11,
                      datetime.time(15, 0): 10,
                      datetime.time(15, 15): 11,
                      datetime.time(15, 30): 11,
                      datetime.time(15, 45): 10,
                      datetime.time(16, 0): 11,
                      datetime.time(16, 15): 11,
                      datetime.time(16, 30): 11,
                      datetime.time(16, 45): 11,
                      datetime.time(17, 0): 11,
                      datetime.time(17, 15): 11,
                      datetime.time(17, 30): 11,
                      datetime.time(17, 45): 11,
                      datetime.time(18, 0): 11,
                      datetime.time(18, 15): 11,
                      datetime.time(18, 30): 11,
                      datetime.time(18, 45): 11,
                      datetime.time(19, 0): 11,
                      datetime.time(19, 15): 11,
                      datetime.time(19, 30): 11,
                      datetime.time(19, 45): 11,
                      datetime.time(20, 0): 11,
                      datetime.time(20, 15): 11,
                      datetime.time(20, 30): 11,
                      datetime.time(20, 45): 12,
                      datetime.time(21, 0): 11,
                      datetime.time(21, 15): 11,
                      datetime.time(21, 30): 11,
                      datetime.time(21, 45): 11,
                      datetime.time(22, 0): 11,
                      datetime.time(22, 15): 11,
                      datetime.time(22, 30): 11,
                      datetime.time(22, 45): 10,
                      datetime.time(23, 0): 10,
                      datetime.time(23, 15): 10,
                      datetime.time(23, 30): 10,
                      datetime.time(23, 45): 9}

    global zipcode_frequency
    zipcode_frequency = {10465.0: 0.01859311526382794,
                         10453.0: 0.06247600924209213,
                         10454.0: 0.04074612553891208,
                         10459.0: 0.049329444422213625,
                         10467.0: 0.061918015706814045,
                         10456.0: 0.08410511323637733,
                         10469.0: 0.03030282820468359,
                         10462.0: 0.03792132958077123,
                         10461.0: 0.03202645763769398,
                         10472.0: 0.041064767265564905,
                         10458.0: 0.0585715365496881,
                         10460.0: 0.05083372978292347,
                         10452.0: 0.05641070102661918,
                         10473.0: 0.03604801263896114,
                         10466.0: 0.036611934392409506,
                         10457.0: 0.07112009236163909,
                         10463.0: 0.029985668532573336,
                         10468.0: 0.04889372038669767,
                         10474.0: 0.013859433054855284,
                         10475.0: 0.02089993315934013,
                         10455.0: 0.044307502604710856,
                         10464.0: 0.002330530768193331,
                         10451.0: 0.054519599430298236,
                         10471.0: 0.008355082483745566,
                         10470.0: 0.008734488446643813,
                         10803.0: 3.482828175042498e-05}

    # each index in the lists refers to the station number, as ordered below
    # with respective number of ambulances
    global stationToZip_dists
    stationToZip_dists = {10465.0: [4.2, 3.0, 5.6, 4.2, 2.1, 1.5, 7.2, 3.0, 1.5, 0.9],
                         10453.0: [3.8, 8.8, 1.8, 3.8, 5.5, 5.3, 2.8, 8.8, 5.3, 6.3],
                         10454.0: [2.5, 6.8, 5.8, 2.5, 5.9, 5.2, 7.4, 6.8, 5.2, 5.9],
                         10459.0: [0.5, 5.4, 3.7, 0.5, 4.4, 3.9, 6.1, 5.4, 3.8, 4.5],
                         10467.0: [6.3, 4.0, 1.7, 4.9, 5.8, 5.7, 0.6, 4.0, 5.7, 6.6],
                         10456.0: [2.2, 6.5, 2.7, 2.2, 5.3, 4.9, 6.6, 6.5, 5.1, 6.1],
                         10469.0: [7.5, 1.5, 2.8, 7.5, 2.4, 4.9, 2.2, 2.5, 4.9, 4.4],
                         10462.0: [2.3, 1.8, 2.4, 2.3, 1.2, 2.2, 4.2, 1.7, 2.2, 4.0],
                         10461.0: [4.9, 1.3, 3.9, 4.9, 0.4, 2.2, 5.6, 1.3, 2.2, 2.1],
                         10472.0: [1.5, 3.9, 3.2, 1.6, 3.0, 1.7, 5.1, 3.9, 1.7, 3.0],
                         10458.0: [4.3, 3.2, 0.3, 4.3, 3.8, 5.0, 2.2, 3.2, 5.0, 6.0],
                         10460.0: [1.4, 2.5, 1.4, 1.4, 2.2, 2.8, 3.2, 2.5, 2.8, 3.7],
                         10452.0: [4.0, 9.0, 3.2, 4.0, 5.7, 5.6, 7.3, 9.0, 5.6, 6.5],
                         10473.0: [3.3, 4.2, 4.4, 3.3, 2.6, 1.2, 6.0, 4.2, 1.2, 3.3],
                         10466.0: [6.7, 3.6, 5.0, 6.7, 4.6, 6.0, 3.3, 3.6, 6.0, 5.5],
                         10457.0: [2.2, 7.2, 1.2, 2.2, 3.9, 3.8, 5.3, 7.2, 3.8, 4.7],
                         10463.0: [7.3, 5.3, 2.8, 9.7, 9.0, 8.2, 1.8, 5.3, 8.9, 9.8],
                         10468.0: [4.9, 3.9, 1.2, 5.0, 4.5, 5.8, 1.5, 4.0, 5.8, 6.7],
                         10474.0: [2.2, 6.5, 5.9, 2.2, 5.5, 5.3, 7.5, 6.9, 5.3, 5.6],
                         10475.0: [7.6, 2.6, 5.2, 7.6, 3.5, 4.9, 6.9, 2.6, 5.1, 4.4],
                         10455.0: [2.1, 7.0, 6.0, 2.1, 6.0, 5.4, 7.6, 7.0, 5.4, 6.1],
                         10464.0: [8.7, 3.7, 6.2, 8.7, 4.6, 6.2, 8.0, 3.7, 6.2, 5.6],
                         10451.0: [5.2, 9.5, 4.6, 2.6, 8.6, 7.9, 6.4, 9.5, 6.9, 7.9],
                         10471.0: [8.8, 13.0, 4.9, 8.4, 8.0, 9.2, 3.7, 7.4, 9.9, 11.0],
                         10470.0: [6.5, 4.5, 4.8, 6.5, 6.1, 7.3, 3.1, 4.5, 7.3, 8.2],
                         10803.0: [8.5, 3.5, 6.0, 8.5, 4.4, 6.0, 7.8, 3.5, 6.0, 5.4]}

    global ambs_by_station
    ambs_by_station = [4, 56, 2, 38, 19, 1, 1, 103, 168, 2]



