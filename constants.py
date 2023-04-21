INITIAL_STATS = {'MAXHP': 25,
                 'HP': 25,
                 'MAXMP': 10,
                 'MP': 10,
                 'ATK': 10,
                 'DEF': 10,
                 'MATK': 10,
                 'MDEF': 10,
                 'SPEED': 10,
                 'CRITCH': 10,
                 'CRITDMG': 10
                 }
STAT_NAMES = ['MAXHP', 'HP', 'MAXMP', 'MP', 'ATK', 'DEF', 'MATK', 'MDEF', 'SPEED', 'CRITCH', 'CRITDMG']
EQUIPMENT_NAMES = ['HELMET', 'ARMOR', 'WEAPON', 'ACCESSORY']
WEAPON_NAMES = ["SWORD", "AXE", "SPEAR", "DAGGER", "STAFF", "BOW"]
FULLY_RECOVER_WHEN_LEVELING_UP = True
STAT_UPGRADE_WHEN_LEVELING_UP = 1
POSSIBLE_PLAYER_ACTIONS = ["NORMAL_ATTACK", "SKILL"]
INITIAL_JOB_DICT = {"Name": "Novice", "lvl": 1, "xp": 0}

# JSON Keys for loading Data
AREAS_KEYS = ["NAME", "NUMBER", "ENEMY_LIST", "BOSS", "DUNGEONS"]
DUNGEON_KEYS = []
ENEMY_KEYS = ["NAME", "STATS", "XP_REWARD", "GOLD_REWARD", "POSSIBLE_LOOT", "LOOT_CHANCE", "SKILLS", "IMAGE_URL", "IS_BOSS"]
EQUIPMENT_KEYS = ["NAME", "DESCRIPTION", "INDIV_VALUE", "OBJECT_TYPE", "EQUIPMENT_TYPE", "STAT_CHANGE_LIST"]
ITEM_KEYS = ["NAME", "DESCRIPTION", "INDIV_VALUE", "OBJECT_TYPE"]
JOB_KEYS = ["NAME", "DESCRIPTION", "SKILL_DICT", "XP_FACTOR"]
SHOP_KEYS = ["AREA_NUMBER", "ITEM_LIST"]
SKILL_KEYS = ["NAME", "DESCRIPTION", "MP_COST", "TYPE", "POWER", "ELEMENT", "STATUS_EFFECT"]
