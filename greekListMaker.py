import os
os.chdir('YOUR FAVORITE DIRECTORY')

import json

data = [
'abac',
'academ',
'acanth',
'acro',
'actin',
'adeno',
'aero',
'aesth',
'aether',
'ether',
'agon',
'gogue',
'agro',
'ailur',
'alcyon',
'aleuro',
'algia',
'algesic',
'allo',
'allel',
'alph',
'alphit',
'amath',
'ambly',
'ammo',
'amnio',
'andr',
'anem',
'anti',
'anth',
'aphrod',
'arachn',
'arch',
'archae',
'arct',
'aret',
'arist',
'arithm',
'arsen',
'arthr',
'arti',
'asco',
'aspr',
'aster',
'astr',
'asthen',
'ather',
'athl',
'aux',
'auto',
'axon',
'bapt',
'baro',
'bary',
'bathy',
'bibl',
'bio',
'blasto',
'blenno',
'botan',
'brachio',
'brachy',
'brady',
'branchi',
'bromat',
'bronch',
'bronto',
'butyr',
'byss',
'caco',
'eccle',
'calyp',
'cardi',
'carp',
'cata',
'cathar',
'caust',
'ceno',
'centr',
'cephal',
'ceram',
'cerat',
'chiro',
'chelon',
'chlor',
'chondr',
'choreo',
'chrom',
'chron',
'chrys',
'cirr',
'clade',
'clado',
'clast',
'clav',
'cleisto',
'cleithr',
'clini',
'cochl',
'coel',
'conic',
'copro',
'corac',
'cosm',
'cosmet',
'cotyl',
'cracy',
'crat',
'crani',
'crepid',
'crico',
'criti',
'crine',
'crypt',
'cryph',
'cten',
'cyan',
'cycl',
'cylind',
'cyn',
'cyst',
'cyt',
'didact',
'dacry',
'dactyl',
'adaman',
'deca',
'delt',
'demo',
'dendr',
'derm',
'despot',
'deuter',
'dexi',
'dia',
'diacosi',
'dino',
'dipl',
'dote',
'dodec',
'dox',
'drama',
'drachm',
'drome',
'droso',
'dryad',
'dyad',
'dyna',
'dys',
'ecc',
'ecto',
'eco',
'eiren',
'electr',
'elem',
'emet',
'enantio',
'encephal',
'endo',
'engy',
'engy',
'ennea',
'eos',
'epi',
'ephed',
'erg',
'org',
'urg',
'erot',
'erythr',
'esot',
'ethi',
'etho',
'ethm',
'ethn',
'etym',
'eur',
'exo',
'galact',
'galax',
'lacto',
'gamo',
'gamy',
'gamet',
'gamm',
'gargal',
'gargar',
'gastr',
'geo',
'geiton',
'gephyr',
'geron',
'geri',
'geran',
'geusia',
'glauc',
'glia',
'gloss',
'glot',
'glute',
'glyc',
'glyph',
'gnath',
'gnom',
'gnos',
'gramm',
'graph',
'gryph',
'gymn',
'gyn',
'gyrin',
'hadro',
'aem',
'hemo',
'hali',
'halo',
'hapl',
'hedo',
'heli',
'hemer',
'hemi',
'hendec',
'hept',
'heres',
'heret',
'heur',
'hex',
'hier',
'hipp',
'ode',
'holi',
'holo',
'homo',
'anoma',
'homeo',
'horo',
'hormo',
'hyal',
'hybr',
'hubr',
'hydn',
'hydr',
'hygr',
'hymen',
'hypo',
'hyph',
'hyo',
'hyper',
'hyph',
'hypn',
'hyps',
'hyster',
'hyen',
'iatr',
'ichthy',
'icos',
'idol',
'ideo',
'iso',
'ischi',
'kilo',
'kine',
'cine',
'klept',
'kudo',
'lamp',
'lecith',
'leio',
'lekan',
'lepid',
'lepto',
'lepro',
'lepsi',
'leuk',
'leuc',
'lipo',
'litan',
'lith',
'logy',
'logist',
'logo',
'logic',
'lys',
'lyti',
'macro',
'magnet',
'mania',
'mechan',
'mega',
'meio',
'melan',
'meliss',
'meno',
'mening',
'meso',
'meta',
'meter',
'metr',
'micro',
'mime',
'mimi',
'mint',
'miso',
'misa',
'mono',
'moron',
'moric',
'moni',
'morph',
'myo',
'mys',
'mycet',
'myco',
'mydr',
'amyl',
'myth',
'myri',
'myrmec',
'myx',
'myz',
'narc',
'naut',
'neo',
'necro',
'nect',
'nemat',
'nephr',
'nesia',
'neur',
'nomy',
'nomic',
'nomia',
'nomad',
'noto',
'notho',
'nyct',
'obel',
'obol',
'ocean',
'ochl',
'oct',
'odont',
'dynia',
'dyne',
'oec',
'oeno',
'phag',
'oestr',
'estro',
'ogdo',
'oid',
'oligo',
'oliga',
'oma',
'ombr',
'ommat',
'omphal',
'onisc',
'onco',
'oneir',
'onio',
'onomat',
'onto',
'onych',
'onym',
'ophi',
'ophthalm',
'opisth',
'opia',
'opsy',
'opt',
'opis',
'opson',
'orog',
'orch',
'orches',
'oreg',
'org',
'organ',
'ornith',
'orphan',
'orth',
'oryz',
'osm',
'oste',
'osto',
'ostrac',
'ostre',
'oxy',
'oxi',
'ozo',
'pach',
'pae',
'pedo',
'paed',
'pedi',
'peda',
'palae',
'paleo',
'palin',
'palim',
'pan',
'para',
'parthen',
'path',
'pater',
'patr',
'pect',
'pelit',
'pelag',
'pelarg',
'pomp',
'penia',
'pent',
'pente',
'pepper',
'pept',
'peri',
'persic',
'petr',
'phae',
'phag',
'phalang',
'phalar',
'pharm',
'phan',
'fant',
'pheno',
'phob',
'phor',
'pheug',
'phyg',
'phil',
'phim',
'phleb',
'phleg',
'phlog',
'phon',
'photo',
'phos',
'phrag',
'phren',
'phron',
'phryn',
'phthleg',
'phyc',
'phyl',
'phys',
'phyt',
'piez',
'pino',
'pirat',
'pirac',
'piso',
'pithec',
'placo',
'place',
'plag',
'plan',
'plas',
'plat',
'plec',
'ploc',
'pleg',
'plect',
'plex',
'plesi',
'pleth',
'pleur',
'plinth',
'pluto',
'pneu',
'pnig',
'pnict',
'pod',
'pogon',
'poe',
'poie',
'pole',
'pola',
'poli',
'poly',
'pomph',
'pore',
'pori',
'poro',
'porn',
'porphyr',
'potam',
'prag',
'pras',
'presby',
'prio',
'priap',
'prism',
'pro',
'psa',
'pseph',
'pseud',
'psil',
'psithyr',
'psittac',
'psoph',
'psor',
'psych',
'pter',
'pto',
'pty',
'pyel',
'pyg',
'pyl',
'pyo',
'pyr',
'pyramid',
'pyrrh',
'raph',
'rhabd',
'rhach',
'rach',
'rhag',
'rheg',
'rheo',
'rhythm',
'rhetin',
'rhig',
'rhin',
'rhiz',
'rhod',
'rhomb',
'rhynch',
'spond',
'spor',
'sacchar',
'salping',
'sapphir',
'sapr',
'sarc',
'saur',
'scalen',
'scandal',
'scaph',
'scat',
'sced',
'scel',
'sceni',
'sceno',
'scene',
'skep',
'scop',
'schem',
'schiz',
'schis',
'scler',
'scolec',
'scoli',
'scombr',
'scoto',
'scyph',
'seism',
'selen',
'sema',
'seri',
'sidero',
'sidere',
'sigm',
'sinap',
'sipho',
'parasit',
'smargd',
'smilo',
'solen',
'soma',
'osome',
'somy',
'soph',
'spasm',
'spast',
'spad',
'sporo',
'spore',
'spele',
'spond',
'spelunk',
'sperm',
'sphal',
'sphen',
'spher',
'sphing',
'sphinct',
'sphondyl',
'sphrag',
'sphyg',
'sphyx',
'spleni',
'spleno',
'stat',
'stasi',
'staphyl',
'steat',
'steg',
'steno',
'steri',
'stereo',
'sternum',
'stetho',
'sthen',
'stich',
'stigm',
'stoch',
'stom',
'strom',
'strat',
'astro',
'stroph',
'strept',
'styg',
'styl',
'sybar',
'syco',
'sym',
'syn',
'sys',
'syring',
'tach',
'taeni',
'taxi',
'taxy',
'taxo',
'tars',
'taur',
'tech',
'criter',
'lesb',
'tekn',
'tele',
'tomy',
'tetart',
'tetr',
'teuch',
'thalam',
'thalass',
'thana',
'thano',
'theo',
'theis',
'thesi',
'theti',
'thema',
'theori',
'thero',
'therap',
'therm',
'thigm',
'thixo',
'thorac',
'thym',
'thyr',
'tonic',
'topi',
'tope',
'toxi',
'trach',
'trag',
'trapez',
'traum',
'treiskaidek',
'trema',
'tri',
'troch',
'trop',
'tryp',
'tympan',
'type',
'typi',
'typo',
'typh',
'tyrann',
'diur',
'urea',
'uria',
'urem',
'uran',
'xanth',
'xen',
'xero',
'xiph',
'xyl',
'eczem',
'zeal',
'zephyr',
'zed',
'zeta',
'zizyph',
'azo',
'zoo',
'zono',
'zone',
'zona',
'zyg',
'zym',
]

with open('greekRootsList.json', 'w') as f:
    json.dump(data, f)
