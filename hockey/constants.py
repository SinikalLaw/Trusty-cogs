BASE_URL = "https://statsapi.web.nhl.com"
HEADSHOT_URL = "https://cms.nhl.bamgrid.com/images/headshots/current/168x168/{}.jpg"
CONTENT_URL = "http://statsapi.web.nhl.com/api/v1/game/{}/content"
CONFIG_ID = 13457745779
TEAMS = {
    "Anaheim Ducks": {
        "away": "#F95602",
        "conference": "Western",
        "division": "Pacific",
        "emoji": "AnaheimDucks:1290853631154720779",
        "home": "#B5985A",
        "id": 24,
        "invite": "https://discord.gg/Pqf9W6M",
        "logo": "https://i.imgur.com/UN3XDe5.png",
        "team_url": "https://www.nhl.com/ducks",
        "timezone": "US/Pacific",
        "nickname": ["ducks", "anaheim"],
        "tri_code": "ANA",
        "active": True,
    },
    "Arizona Coyotes": {
        "away": "#E2D6B5",
        "conference": "Western",
        "division": "Central",
        "emoji": "ArizonaCoyotes:897522654561583155",
        "home": "#8C2633",
        "id": 53,
        "invite": "https://discord.gg/ebGC7rP",
        "logo": "https://i.imgur.com/nCdFkHP.png",
        "team_url": "https://www.nhl.com/coyotes",
        "timezone": "US/Arizona",
        "nickname": ["yotes", "arizona", "coyotes"],
        "tri_code": "ARI",
        "active": False,
    },
    "Boston Bruins": {
        "away": "#111111",
        "conference": "Eastern",
        "division": "Atlantic",
        "emoji": "BostonBruins:1290853621860270133",
        "home": "#FCB514",
        "id": 6,
        "invite": "https://discord.gg/BbPN25d",
        "logo": "https://i.imgur.com/wQmOHWJ.png",
        "team_url": "https://www.nhl.com/bruins",
        "timezone": "US/Eastern",
        "nickname": ["bruins", "boston"],
        "tri_code": "BOS",
        "active": True,
    },
    "Buffalo Sabres": {
        "away": "#FCB514",
        "conference": "Eastern",
        "division": "Atlantic",
        "emoji": "BuffaloSabres:1290853611345018972",
        "home": "#002654",
        "id": 7,
        "invite": "https://discord.gg/C6gpAvqDWm",
        "logo": "https://i.imgur.com/GKxSQaT.png",
        "team_url": "https://www.nhl.com/sabres",
        "timezone": "US/Eastern",
        "nickname": ["sabres", "buffalo"],
        "tri_code": "BUF",
        "active": True,
    },
    "Calgary Flames": {
        "away": "#F1BE48",
        "conference": "Western",
        "division": "Pacific",
        "emoji": "CalgaryFlames:1290853595557658654",
        "home": "#B72B35",
        "id": 20,
        "invite": "https://discord.gg/7fYbvP9VqM",
        "logo": "https://i.imgur.com/ZYdIdeI.png",
        "team_url": "https://www.nhl.com/flames",
        "timezone": "US/Mountain",
        "nickname": ["flames", "calgary"],
        "tri_code": "CGY",
        "active": True,
    },
    "Carolina Hurricanes": {
        "away": "#A4A9AD",
        "conference": "Eastern",
        "division": "Metropolitan",
        "emoji": "CarolinaHurricanes:1290853577346121829",
        "home": "#B72B35",
        "id": 12,
        "invite": "https://discord.gg/mqGDdrr",
        "logo": "https://i.imgur.com/uZrY3uS.png",
        "team_url": "https://www.nhl.com/hurricanes",
        "timezone": "US/Eastern",
        "nickname": ["canes", "carolina", "hurricanes"],
        "tri_code": "CAR",
        "active": True,
    },
    "Chicago Blackhawks": {
        "away": "#000000",
        "conference": "Western",
        "division": "Central",
        "emoji": "ChicagoBlackhawks:1290853357468123258",
        "home": "#CF0A2C",
        "id": 16,
        "invite": "https://discord.gg/WbXXanjz23",
        "logo": "https://i.imgur.com/X3vyFkn.png",
        "team_url": "https://www.nhl.com/blackhawks",
        "timezone": "US/Central",
        "nickname": ["hawks", "chicago", "blackhawks"],
        "tri_code": "CHI",
        "active": True,
    },
    "Colorado Avalanche": {
        "away": "#236192",
        "conference": "Western",
        "division": "Central",
        "emoji": "ColoradoAvalanche:1290853339730542612",
        "home": "#6F263D",
        "id": 21,
        "invite": "https://discord.gg/HzvKebH",
        "logo": "https://i.imgur.com/TvIgzF5.png",
        "team_url": "https://www.nhl.com/avalanche",
        "timezone": "US/Mountain",
        "nickname": ["avs", "avalanche", "colorado"],
        "tri_code": "COL",
        "active": True,
    },
    "Columbus Blue Jackets": {
        "away": "#CE1126",
        "conference": "Eastern",
        "division": "Metropolitan",
        "emoji": "ColumbusBlueJackets:1290853329852698625",
        "home": "#041E42",
        "id": 29,
        "invite": "https://discord.gg/wJKdYtG",
        "logo": "https://i.imgur.com/TrsQ4rZ.png",
        "team_url": "https://www.nhl.com/bluejackets",
        "timezone": "US/Eastern",
        "nickname": ["jackets", "bjs", "columbus"],
        "tri_code": "CBJ",
        "active": True,
    },
    "Dallas Stars": {
        "away": "#8F8F8C",
        "conference": "Western",
        "division": "Central",
        "emoji": "DallasStars:1290853557578502174",
        "home": "#006847",
        "id": 25,
        "invite": "https://discord.gg/uNdH6hX",
        "logo": "https://i.imgur.com/SsmVVsv.png",
        "team_url": "https://www.nhl.com/stars",
        "timezone": "US/Central",
        "nickname": ["stars", "dallas"],
        "tri_code": "DAL",
        "active": True,
    },
    "Detroit Red Wings": {
        "away": "#FFFFFF",
        "conference": "Eastern",
        "division": "Atlantic",
        "emoji": "DetroitRedWings:1290853315856302120",
        "home": "#C8102E",
        "id": 17,
        "invite": "https://discord.gg/UzvNY9srvJ",
        "logo": "https://i.imgur.com/TO68V0m.png",
        "team_url": "https://www.nhl.com/redwings",
        "timezone": "US/Eastern",
        "nickname": ["red wings", "detroit", "wings"],
        "tri_code": "DET",
        "active": True,
    },
    "Edmonton Oilers": {
        "away": "#041E41",
        "conference": "Western",
        "division": "Pacific",
        "emoji": "EdmontonOilers:1290853544785870960",
        "home": "#FF4C00",
        "id": 22,
        "invite": "https://discord.gg/6XKZyxy",
        "logo": "https://i.imgur.com/xu4SFJR.png",
        "team_url": "https://www.nhl.com/oilers",
        "timezone": "US/Mountain",
        "nickname": ["oilers", "edmonton"],
        "tri_code": "EDM",
        "active": True,
    },
    "Florida Panthers": {
        "away": "#041E42",
        "conference": "Eastern",
        "division": "Atlantic",
        "emoji": "FloridaPanthers:1290853523994574991",
        "home": "#C8102E",
        "id": 13,
        "invite": "https://discord.gg/HsPmCmth7W",
        "logo": "https://i.imgur.com/aNuTh9j.png",
        "team_url": "https://www.nhl.com/panthers",
        "timezone": "US/Eastern",
        "nickname": ["panthers", "florida"],
        "tri_code": "FLA",
        "active": True,
    },
    "Los Angeles Kings": {
        "away": "#B2B7BB",
        "conference": "Western",
        "division": "Pacific",
        "emoji": "LosAngelesKings:1290853512590262384",
        "home": "#111111",
        "id": 26,
        "invite": "https://discord.gg/H6EH73h",
        "logo": "https://i.imgur.com/Ny6r9tI.png",
        "team_url": "https://www.nhl.com/kings",
        "timezone": "US/Pacific",
        "nickname": ["kings", "la"],
        "tri_code": "LAK",
        "active": True,
    },
    "Minnesota Wild": {
        "away": "#C51230",
        "conference": "Western",
        "division": "Central",
        "emoji": "MinnesotaWild:1290853304812961914",
        "home": "#004F30",
        "id": 30,
        "invite": "https://discord.gg/CT2HUUV",
        "logo": "https://i.imgur.com/zNfco8g.png",
        "team_url": "https://www.nhl.com/wild",
        "timezone": "US/Central",
        "nickname": ["wild", "minnesota"],
        "tri_code": "MIN",
        "active": True,
    },
    "Montréal Canadiens": {
        "away": "#192168",
        "conference": "Eastern",
        "division": "Atlantic",
        "emoji": "MontrealCanadiens:1290853500955262998",
        "home": "#AF1E2D",
        "id": 8,
        "invite": "https://discord.gg/rhabs",
        "logo": "https://i.imgur.com/HcqfsbC.png",
        "team_url": "https://www.nhl.com/canadiens",
        "timezone": "US/Eastern",
        "nickname": ["montreal canadiens", "habs", "montreal", "canadiens"],
        "tri_code": "MTL",
        "active": True,
    },
    "Nashville Predators": {
        "away": "#041E42",
        "conference": "Western",
        "division": "Central",
        "emoji": "NashvillePredators:1290853293236420680",
        "home": "#FFB81C",
        "id": 18,
        "invite": "https://discord.com/invite/v3fZbxAdzu",
        "logo": "https://i.imgur.com/amrR0vN.png",
        "team_url": "https://www.nhl.com/predators",
        "timezone": "US/Central",
        "nickname": ["preds", "predators", "nashville"],
        "tri_code": "NSH",
        "active": True,
    },
    "New Jersey Devils": {
        "away": "#000000",
        "conference": "Eastern",
        "division": "Metropolitan",
        "emoji": "NewJerseyDevils:1290853281018675200",
        "home": "#E03A3E",
        "id": 1,
        "invite": "https://discord.gg/njdevils",
        "logo": "https://i.imgur.com/KUOXIZO.png",
        "team_url": "https://www.nhl.com/devils",
        "timezone": "US/Eastern",
        "nickname": ["devils", "new jersey"],
        "tri_code": "NJD",
        "active": True,
    },
    "New York Islanders": {
        "away": "#F47920",
        "conference": "Eastern",
        "division": "Metropolitan",
        "emoji": "NewYorkIslanders:1290853268091834458",
        "home": "#00529B",
        "id": 2,
        "invite": "https://discord.gg/MSHNyqB",
        "logo": "https://i.imgur.com/56vercO.png",
        "team_url": "https://www.nhl.com/islanders",
        "timezone": "US/Eastern",
        "nickname": ["isles", "islanders"],
        "tri_code": "NYI",
        "active": True,
    },
    "New York Rangers": {
        "away": "#C8102E",
        "conference": "Eastern",
        "division": "Metropolitan",
        "emoji": "NewYorkRangers:1290853248865140736",
        "home": "#0038A8",
        "id": 3,
        "invite": "https://discord.gg/rrjvywb",
        "logo": "https://i.imgur.com/E9JSATK.png",
        "team_url": "https://www.nhl.com/nyrangers",
        "timezone": "US/Eastern",
        "nickname": ["rangers"],
        "tri_code": "NYR",
        "active": True,
    },
    "Ottawa Senators": {
        "away": "#CBA044",
        "conference": "Eastern",
        "division": "Atlantic",
        "emoji": "OttawaSenators:1290853486770131057",
        "home": "#E31837",
        "id": 9,
        "invite": "https://discord.gg/xPkughF2xr",
        "logo": "https://i.imgur.com/HGvOFDf.png",
        "team_url": "https://www.nhl.com/senators",
        "timezone": "US/Eastern",
        "nickname": ["sens", "senators", "ottawa"],
        "tri_code": "OTT",
        "active": True,
    },
    "Philadelphia Flyers": {
        "away": "#000000",
        "conference": "Eastern",
        "division": "Metropolitan",
        "emoji": "PhiladelphiaFlyers:1290853471758717008",
        "home": "#F74902",
        "id": 4,
        "invite": "https://discord.gg/WwG2MFf",
        "logo": "https://i.imgur.com/tQ5oRTq.png",
        "team_url": "https://www.nhl.com/flyers",
        "timezone": "US/Eastern",
        "nickname": ["flyers", "philly", "philadelphia"],
        "tri_code": "PHI",
        "active": True,
    },
    "Pittsburgh Penguins": {
        "away": "#CFC493",
        "conference": "Eastern",
        "division": "Metropolitan",
        "emoji": "PittsburghPenguins:1290853448551632946",
        "home": "#FCB514",
        "id": 5,
        "invite": "https://discord.gg/FkAUtvs",
        "logo": "https://i.imgur.com/5pfb5zw.png",
        "team_url": "https://www.nhl.com/penguins",
        "timezone": "US/Eastern",
        "nickname": ["pens", "penguins", "pittsburgh"],
        "tri_code": "PIT",
        "active": True,
    },
    "San Jose Sharks": {
        "away": "#EA7200",
        "conference": "Western",
        "division": "Pacific",
        "emoji": "SanJoseSharks:1290853238962388992",
        "home": "#006D75",
        "id": 28,
        "invite": "https://discord.gg/X9Xr8Zn",
        "logo": "https://i.imgur.com/5RiH6zW.png",
        "team_url": "https://www.nhl.com/sharks",
        "timezone": "US/Pacific",
        "nickname": ["sharks", "san jose"],
        "tri_code": "SJS",
        "active": True,
    },
    "Seattle Kraken": {
        "away": "#5dbcd2",
        "conference": "Western",
        "division": "Pacific",
        "emoji": "SeattleKraken:1290853434920276069",
        "home": "#0C1A28",
        "id": 55,
        "invite": "https://discord.gg/ajgvaXWHBQ",
        "logo": "https://i.imgur.com/wAyOxLg.png",
        "team_url": "https://www.nhl.com/kraken",
        "timezone": "US/Pacific",
        "nickname": ["kraken", "seattle"],
        "tri_code": "SEA",
        "active": True,
    },
    "St. Louis Blues": {
        "away": "#FCB514",
        "conference": "Western",
        "division": "Central",
        "emoji": "StLouisBlues:1290853228744802355",
        "home": "#002F87",
        "id": 19,
        "invite": "https://discord.gg/013pcvc9v5MCl64Ic",
        "logo": "https://i.imgur.com/jjZV8SO.png",
        "team_url": "https://www.nhl.com/blues",
        "timezone": "US/Central",
        "nickname": ["blues", "st. louis"],
        "tri_code": "STL",
        "active": True,
    },
    "Tampa Bay Lightning": {
        "away": "#FFFFFF",
        "conference": "Eastern",
        "division": "Atlantic",
        "emoji": "TampaBayLightning:1290853419816321126",
        "home": "#002868",
        "id": 14,
        "invite": "https://discord.gg/WjNvprr",
        "logo": "https://i.imgur.com/nVM37o4.png",
        "team_url": "https://www.nhl.com/lightning",
        "timezone": "US/Eastern",
        "nickname": ["bolts", "lightning", "tampa"],
        "tri_code": "TBL",
        "active": True,
    },
    "Team Atlantic": {
        "away": "#fef5aa",
        "conference": "",
        "division": "",
        "emoji": "Atlantic:1291958601589719141",
        "home": "#032c88",
        "id": 87,
        "invite": "No Server Found",
        "logo": "https://i.imgur.com/I1NWsss.png",
        "team_url": "http://nhl.coms.com",
        "timezone": "US/Eastern",
        "nickname": [],
        "tri_code": "",
        "active": False,
    },
    "Team Central": {
        "away": "#111111",
        "conference": "",
        "division": "",
        "emoji": "Central:1291958592722833609",
        "home": "#ff6668",
        "id": 89,
        "invite": "No Server Found",
        "logo": "https://i.imgur.com/Adrh7aD.png",
        "team_url": "http://nhl.coms.com",
        "timezone": "US/Central",
        "nickname": [],
        "tri_code": "",
        "active": False,
    },
    "Team Metropolitan": {
        "away": "#d1cad2",
        "conference": "",
        "division": "",
        "emoji": "Metropolitan:1291958583361142897",
        "home": "#f6e98b",
        "id": 88,
        "invite": "No Server Found",
        "logo": "https://i.imgur.com/l4nxmZx.png",
        "team_url": "http://nhl.coms.com",
        "timezone": "US/Mountain",
        "nickname": [],
        "tri_code": "",
        "active": False,
    },
    "Team Pacific": {
        "away": "#FFFFFF",
        "conference": "",
        "division": "",
        "emoji": "Pacific:1291958564788764743",
        "home": "#ff2734",
        "id": 90,
        "invite": "No Server Found",
        "logo": "https://i.imgur.com/e5a4y36.png",
        "team_url": "http://nhl.coms.com",
        "timezone": "US/Pacific",
        "nickname": [],
        "tri_code": "",
        "active": False,
    },
    "Toronto Maple Leafs": {
        "away": "#FFFFFF",
        "conference": "Eastern",
        "division": "Atlantic",
        "emoji": "TorontoMapleLeafs:1290853216199770163",
        "home": "#003E7E",
        "id": 10,
        "invite": "https://discord.gg/leafs",
        "logo": "https://i.imgur.com/74QfPKT.png",
        "team_url": "http://www.mapleleafs.com",
        "timezone": "US/Eastern",
        "nickname": ["leafs", "toronto", "maple leafs"],
        "tri_code": "TOR",
        "active": True,
    },
    "Utah Hockey Club": {
        "away": "#FFFFFF",
        "conference": "Western",
        "division": "Central",
        "emoji": "UtahHockeyClub:1290853401319444592",
        "home": "#70ade2",
        "id": 59,
        "invite": "https://discord.gg/8xRq64XWEE",
        "logo": "https://i.imgur.com/JKSc5ZV.png",
        "team_url": "",
        "timezone": "US/Mountain",
        "nickname": ["utah"],
        "tri_code": "UTA",
        "active": True,
    },
    "Vancouver Canucks": {
        "away": "#008852",
        "conference": "Western",
        "division": "Pacific",
        "emoji": "VancouverCanucks:1290853386849226832",
        "home": "#001F5C",
        "id": 23,
        "invite": "https://discord.gg/UTZ5Vrb",
        "logo": "https://i.imgur.com/OvRu1Hw.png",
        "team_url": "http://www.canucks.com",
        "timezone": "US/Pacific",
        "nickname": ["canucks", "nucks", "nuks", "vancouver"],
        "tri_code": "VAN",
        "active": True,
    },
    "Vegas Golden Knights": {
        "away": "#333F42",
        "conference": "Western",
        "division": "Pacific",
        "emoji": "VegasGoldenKnights:1290853374086086768",
        "home": "#B4975A",
        "id": 54,
        "invite": "https://discord.gg/pPEQQPmm9q",
        "logo": "https://i.imgur.com/wg4A439.png",
        "team_url": "https://www.nhl.com/goldenknights",
        "timezone": "US/Pacific",
        "nickname": ["knights", "vegas"],
        "tri_code": "VGK",
        "active": True,
    },
    "Washington Capitals": {
        "away": "#CF0A2C",
        "conference": "Eastern",
        "division": "Metropolitan",
        "emoji": "WashingtonCapitals:1290853206846476289",
        "home": "#041E41",
        "id": 15,
        "invite": "https://discord.gg/2HXAJm23Ph",
        "logo": "https://i.imgur.com/NTEqbzE.png",
        "team_url": "https://www.nhl.com/capitals",
        "timezone": "US/Eastern",
        "nickname": ["caps", "washington", "capitals"],
        "tri_code": "WSH",
        "active": True,
    },
    "Winnipeg Jets": {
        "away": "#AC162C",
        "conference": "Western",
        "division": "Central",
        "emoji": "WinnipegJets:1290853193173041172",
        "home": "#041E41",
        "id": 52,
        "invite": "https://discord.gg/Q7bm7ZK8QG",
        "logo": "https://i.imgur.com/M4dFABA.png",
        "team_url": "https://www.nhl.com/jets",
        "timezone": "US/Central",
        "nickname": ["jets", "winnipeg"],
        "tri_code": "WPG",
        "active": True,
    },
    "Montreal Wanderers": {
        "conference": "",
        "division": "",
        "id": 41,
        "logo": "https://i.imgur.com/6ksA0hH.png",
        "tri_code": "MWN",
        "away": "#000000",
        "home": "#000000",
        "emoji": "MontrealWanderers:747413468755394600",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "St. Louis Eagles": {
        "conference": "",
        "division": "",
        "id": 45,
        "logo": "https://i.imgur.com/ehHaKTP.png",
        "tri_code": "SLE",
        "away": "#000000",
        "home": "#000000",
        "emoji": "StLouisEagles:747409678417526895",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Hamilton Tigers": {
        "conference": "",
        "division": "",
        "id": 37,
        "logo": "https://i.imgur.com/le8g7kW.png",
        "tri_code": "HAM",
        "away": "#000000",
        "home": "#000000",
        "emoji": "HamiltonTigers:747409674957094913",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Montreal Maroons": {
        "conference": "",
        "division": "",
        "id": 43,
        "logo": "https://i.imgur.com/LGotJwK.png",
        "tri_code": "MMR",
        "away": "#000000",
        "home": "#000000",
        "emoji": "MontrealMaroons:747409674843717712",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Brooklyn Americans": {
        "conference": "",
        "division": "",
        "id": 51,
        "logo": "https://i.imgur.com/b7wDd9v.png",
        "tri_code": "NYA",
        "away": "#000000",
        "home": "#000000",
        "emoji": "BrooklynAmericans:747409673447014453",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Philadelphia Quakers": {
        "conference": "",
        "division": "",
        "id": 39,
        "logo": "https://i.imgur.com/RIyBZmz.png",
        "tri_code": "PIR",
        "away": "#000000",
        "home": "#000000",
        "emoji": "PhiladelphiaQuakers:747409676655657081",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Cleveland Barons": {
        "conference": "",
        "division": "",
        "id": 46,
        "logo": "https://i.imgur.com/ummTel7.png",
        "tri_code": "OAK",
        "away": "#000000",
        "home": "#000000",
        "emoji": "ClevelandBarons:747409678308343819",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Ottawa Senators (1917)": {
        "conference": "",
        "division": "",
        "id": 36,
        "logo": "https://i.imgur.com/wLtNlq0.png",
        "tri_code": "SEN",
        "away": "#000000",
        "home": "#000000",
        "emoji": "OttawaSenators:747409677784055828",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Quebec Bulldogs": {
        "conference": "",
        "division": "",
        "id": 42,
        "logo": "https://i.imgur.com/vbxASOv.png",
        "tri_code": "QBD",
        "away": "#000000",
        "home": "#000000",
        "emoji": "QuebecBulldogs:747409675787698216",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Toronto Arenas": {
        "conference": "",
        "division": "",
        "id": 57,
        "logo": "https://i.imgur.com/auKTjWh.png",
        "tri_code": "TAN",
        "away": "#000000",
        "home": "#000000",
        "emoji": "TorontoArenas:747409674860494919",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Toronto St. Patricks": {
        "conference": "",
        "division": "",
        "id": 58,
        "logo": "https://i.imgur.com/xQp3Hqn.png",
        "tri_code": "TSP",
        "away": "#000000",
        "home": "#000000",
        "emoji": "TorontoStPatricks:747409677624803368",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "New York Americans": {
        "conference": "",
        "division": "",
        "id": 44,
        "logo": "https://i.imgur.com/q7YXoLM.png",
        "tri_code": "NYA",
        "away": "#000000",
        "home": "#000000",
        "emoji": "NewYorkAmericans:747409678346092654",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Pittsburgh Pirates": {
        "conference": "",
        "division": "",
        "id": 38,
        "logo": "https://i.imgur.com/dsFuIsp.png",
        "tri_code": "PIR",
        "away": "#000000",
        "home": "#000000",
        "emoji": "PittsburghPirates:747409678480179310",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Detroit Cougars": {
        "conference": "",
        "division": "",
        "id": 40,
        "logo": "https://i.imgur.com/r63YuFI.png",
        "tri_code": "DCG",
        "away": "#000000",
        "home": "#000000",
        "emoji": "DetroitCougars:747409675149901835",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Detroit Falcons": {
        "conference": "",
        "division": "",
        "id": 50,
        "logo": "https://i.imgur.com/WDZdGXV.png",
        "tri_code": "DFL",
        "away": "#000000",
        "home": "#000000",
        "emoji": "DetroitFalcons:747409678295629854",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Oakland Seals": {
        "conference": "",
        "division": "",
        "id": 46,
        "logo": "https://i.imgur.com/Qf8QS5q.png",
        "tri_code": "OAK",
        "away": "#000000",
        "home": "#000000",
        "emoji": "OaklandSeals:747409678278852608",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "California Golden Seals": {
        "conference": "",
        "division": "",
        "id": 56,
        "logo": "https://i.imgur.com/RFNfdkj.png",
        "tri_code": "CGS",
        "away": "#000000",
        "home": "#000000",
        "emoji": "CaliforniaGoldenSeals:747409676127436854",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Minnesota North Stars": {
        "conference": "Prince of Wales",
        "division": "Norris",
        "id": 31,
        "logo": "https://i.imgur.com/iaIpyke.png",
        "tri_code": "MNS",
        "away": "#000000",
        "home": "#000000",
        "emoji": "MinnesotaNorthStars:747409676462719026",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Atlanta Flames": {
        "conference": "",
        "division": "",
        "id": 47,
        "logo": "https://i.imgur.com/SuPIGnQ.png",
        "tri_code": "AFM",
        "away": "#000000",
        "home": "#000000",
        "emoji": "AtlantaFlames:747409673371779072",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Colorado Rockies": {
        "conference": "",
        "division": "",
        "id": 35,
        "logo": "https://i.imgur.com/u7099Fp.png",
        "tri_code": "CLR",
        "away": "#000000",
        "home": "#000000",
        "emoji": "ColoradoRockies:747409677394116690",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Kansas City Scouts": {
        "conference": "",
        "division": "",
        "id": 48,
        "logo": "https://i.imgur.com/Z05dKee.png",
        "tri_code": "KCS",
        "away": "#000000",
        "home": "#000000",
        "emoji": "KansasCityScouts:747409678773911602",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Hartford Whalers": {
        "conference": "Prince of Wales",
        "division": "Adams",
        "id": 34,
        "logo": "https://i.imgur.com/HEhXCdm.png",
        "tri_code": "HFD",
        "away": "#000000",
        "home": "#000000",
        "emoji": "HartfordWhalers:747409677339459595",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Quebec Nordiques": {
        "conference": "Prince of Wales",
        "division": "Adams",
        "id": 32,
        "logo": "https://i.imgur.com/i6sMDMv.png",
        "tri_code": "QUE",
        "away": "#000000",
        "home": "#000000",
        "emoji": "QuebecNordiques:747409676898926642",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Phoenix Coyotes": {
        "conference": "Western",
        "division": "Pacific",
        "id": 27,
        "logo": "https://i.imgur.com/FIxCOnj.png",
        "tri_code": "PHX",
        "away": "#000000",
        "home": "#000000",
        "emoji": "PhoenixCoyotes:747409679193341952",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Winnipeg Jets (1979)": {
        "conference": "Clarence Campbell",
        "division": "Smythe",
        "id": 33,
        "logo": "https://i.imgur.com/otWBB2N.png",
        "tri_code": "WIN",
        "away": "#000000",
        "home": "#000000",
        "emoji": "WinnipegJets:747409678304280637",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Atlanta Thrashers": {
        "conference": "",
        "division": "",
        "id": 11,
        "logo": "https://i.imgur.com/7jYCLTD.png",
        "tri_code": "ATL",
        "away": "#000000",
        "home": "#000000",
        "emoji": "AtlantaThrashers:747409677247315987",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Team Honda West": {
        "conference": "",
        "division": "Honda West",
        "id": 11,
        "logo": "https://cdn.discordapp.com/attachments/440178442886053888/796832213060550686/9110__national_hockey_league-division-2021.png",
        "tri_code": "THW",
        "away": "#000000",
        "home": "#000000",
        "emoji": "",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Team MassMutual East": {
        "conference": "",
        "division": "MassMutual East",
        "id": 11,
        "logo": "https://cdn.discordapp.com/attachments/440178442886053888/796832177836785684/9017__national_hockey_league-division-2021.png",
        "tri_code": "THW",
        "away": "#000000",
        "home": "#000000",
        "emoji": "",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Team Scotia North": {
        "conference": "",
        "division": "Scotia North",
        "id": 11,
        "logo": "https://cdn.discordapp.com/attachments/440178442886053888/796832087733960765/1380__national_hockey_league-division-2021.png",
        "tri_code": "THW",
        "away": "#000000",
        "home": "#000000",
        "emoji": "",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
    "Team Discover Central": {
        "conference": "",
        "division": "Discover Central",
        "id": 11,
        "logo": "https://cdn.discordapp.com/attachments/440178442886053888/796832145779720242/3662__national_hockey_league-division-2021.png",
        "tri_code": "THW",
        "away": "#000000",
        "home": "#000000",
        "emoji": "",
        "timezone": "US/Eastern",
        "team_url": "",
        "nickname": [],
        "invite": "No Server Found",
        "active": False,
    },
}
if __name__ == "__main__":
    import re

    for name, team in TEAMS.items():
        if "i.imgur" in team["logo"]:
            continue
        if "imgur" not in team["logo"]:
            continue
        code = re.search(r"https:\/\/imgur\.com\/(\w+)", team["logo"])
        new_url = f"https://i.imgur.com/{code.group(1)}.png"
        team["logo"] = new_url
    print(TEAMS)
