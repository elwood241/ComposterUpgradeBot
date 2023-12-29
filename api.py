import mysql.connector
import os
from dotenv import dotenv_values
config = dotenv_values(".env")




def connectdb():
    db = mysql.connector.connect(
    host=config["IP"],
    port=config["PORT"],
    user=config["USER"],
    passwd=config["PASSWORD"],
    database=config["DBNAME"],
    )
    return db



def createTables():
    print("tables are creating..")
    db = connectdb()
    mycursor = db.cursor(buffered=True)
    tableQuerrys = [
        """CREATE TABLE IF NOT EXISTS ComposterSpeed (
            id VARCHAR(32) NOT NULL,
            PRIMARY KEY(id),
            required_copper INTEGER DEFAULT 35650,
            required_tighly_tied_haybale INTEGER DEFAULT 83,
            required_hay_bale INTEGER DEFAULT 112,
            required_ench_golden_carrot INTEGER DEFAULT 1166,
            required_cropie INTEGER DEFAULT 245,
            required_squash INTEGER DEFAULT 245,
            required_fermento INTEGER DEFAULT 21,
            required_condensed_fermento INTEGER DEFAULT 25,
            
            acquired_copper INTEGER DEFAULT 0,
            acquired_tighly_tied_haybale INTEGER DEFAULT 0,
            acquired_hay_bale INTEGER DEFAULT 0,
            acquired_ench_golden_carrot INTEGER DEFAULT 0,
            acquired_cropie INTEGER DEFAULT 0,
            acquired_squash INTEGER DEFAULT 0,
            acquired_fermento INTEGER DEFAULT 0,
            acquired_condensed_fermento INTEGER DEFAULT 0            
        ); """,
            
        """CREATE TABLE IF NOT EXISTS MultiDrop (
            id VARCHAR(32) NOT NULL,
            PRIMARY KEY(id),
            required_copper INTEGER DEFAULT 35650,
            required_ench_baked_potato INTEGER DEFAULT 1167,
            required_ench_pumpkin INTEGER DEFAULT 64,
            required_polished_pumpkin INTEGER DEFAULT 591,
            required_cropie INTEGER DEFAULT 245,
            required_squash INTEGER DEFAULT 245,
            required_fermento INTEGER DEFAULT 21,
            required_condensed_fermento INTEGER DEFAULT 25,
            
            acquired_copper INTEGER DEFAULT 0,
            acquired_ench_baked_potato INTEGER DEFAULT 0,
            acquired_ench_pumpkin INTEGER DEFAULT 0,
            acquired_polished_pumpkin INTEGER DEFAULT 0,
            acquired_cropie INTEGER DEFAULT 0,
            acquired_squash INTEGER DEFAULT 0,
            acquired_fermento INTEGER DEFAULT 0,
            acquired_condensed_fermento INTEGER DEFAULT 0
                
        )""",
        
        """CREATE TABLE IF NOT EXISTS FuelCap (
            id VARCHAR(32) NOT NULL,
            PRIMARY KEY(id),
            required_copper INTEGER DEFAULT 35650,
            required_ench_sugar_cane INTEGER DEFAULT 1167,
            required_ench_melon_block INTEGER DEFAULT 1740,
            required_cropie INTEGER DEFAULT 245,
            required_squash INTEGER DEFAULT 245,
            required_fermento INTEGER DEFAULT 21,
            required_condensed_fermento INTEGER DEFAULT 25,
            
            acquired_copper INTEGER DEFAULT 0,
            acquired_ench_sugar_cane INTEGER DEFAULT 0,
            acquired_ench_melon_block INTEGER DEFAULT 0,
            acquired_cropie INTEGER DEFAULT 0,
            acquired_squash INTEGER DEFAULT 0,
            acquired_fermento INTEGER DEFAULT 0,
            acquired_condensed_fermento INTEGER DEFAULT 0
                
        )""",
        
        """CREATE TABLE IF NOT EXISTS OrganicMatterCap (
            id VARCHAR(32) NOT NULL,
            PRIMARY KEY(id),
            required_copper INTEGER DEFAULT 35650,
            required_ench_cactus INTEGER DEFAULT 592,
            required_ench_cookie INTEGER DEFAULT 1653,
            required_cropie INTEGER DEFAULT 245,
            required_squash INTEGER DEFAULT 245,
            required_fermento INTEGER DEFAULT 21,
            required_condensed_fermento INTEGER DEFAULT 25,
            
            acquired_copper INTEGER DEFAULT 0,
            acquired_ench_cactus INTEGER DEFAULT 0,
            acquired_ench_cookie INTEGER DEFAULT 0,
            acquired_cropie INTEGER DEFAULT 0,
            acquired_squash INTEGER DEFAULT 0,
            acquired_fermento INTEGER DEFAULT 0,
            acquired_condensed_fermento INTEGER DEFAULT 0
                
        )""",
        
        """CREATE TABLE IF NOT EXISTS CostReduction (
            id VARCHAR(32) NOT NULL,
            PRIMARY KEY(id),
            required_copper INTEGER DEFAULT 35650,
            required_ench_brown_mushroom INTEGER DEFAULT 32,
            required_mutant_nether_wart INTEGER DEFAULT 943,
            required_ench_brown_mushroom_block INTEGER DEFAULT 2660,
            required_ench_red_mushroom_block INTEGER DEFAULT 2026,
            required_cropie INTEGER DEFAULT 245,
            required_squash INTEGER DEFAULT 245,
            required_fermento INTEGER DEFAULT 21,
            required_condensed_fermento INTEGER DEFAULT 25,
            
            acquired_copper INTEGER DEFAULT 0,
            acquired_ench_brown_mushroom INTEGER DEFAULT 0,
            acquired_mutant_nether_wart INTEGER DEFAULT 0,
            acquired_ench_brown_mushroom_block INTEGER DEFAULT 0,
            acquired_ench_red_mushroom_block INTEGER DEFAULT 0,
            acquired_cropie INTEGER DEFAULT 0,
            acquired_squash INTEGER DEFAULT 0,
            acquired_fermento INTEGER DEFAULT 0,
            acquired_condensed_fermento INTEGER DEFAULT 0
                
        )"""
    ]
    
    

    for querry in tableQuerrys:
        if "ALTER" in querry:
            try:
                mycursor.execute(querry)
            except:
                pass
        else:
            try:
                mycursor.execute(querry)
            except Exception as e:
                print("I had a Error in the Querry: ", querry, "\n The Error: ", e)
    db.commit()
    print("Tables created.")
    
def createCompostUpgrades(id):
    db = connectdb()
    cursor = db.cursor(buffered=True)

    cursor.execute(
        'INSERT INTO ComposterSpeed (id) VALUES (%s)', (id,)
    )
    cursor.execute(
        'INSERT INTO MultiDrop (id) VALUES (%s)', (id,)
    )
    cursor.execute(
        'INSERT INTO FuelCap (id) VALUES (%s)', (id,)
    )
    cursor.execute(
        'INSERT INTO OrganicMatterCap (id) VALUES (%s)', (id,)
    )
    cursor.execute(
        'INSERT INTO CostReduction (id) VALUES (%s)', (id,)
    )
    
    db.commit()

def getComposterSpeed(id):
    db = connectdb()
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM ComposterSpeed WHERE id = %s", (id,))    
    return cursor.fetchone()


def getCostReduction(id):
    db = connectdb()
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM CostReduction WHERE id = %s", (id,))    
    return cursor.fetchone()


def getFuelCap(id):
    db = connectdb()
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM FuelCap WHERE id = %s", (id,))    
    return cursor.fetchone()


def getMultiDrop(id):
    db = connectdb()
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM MultiDrop WHERE id = %s", (id,))    
    return cursor.fetchone()


def getOrganicMatterCap(id):
    db = connectdb()
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM OrganicMatterCap WHERE id = %s", (id,))    
    return cursor.fetchone()
    
    
    
    

def increaseComposterSpeed(id, copper=0,
                      tighly_tied_haybale=0, hay_bale=0,
                      ench_golden_carrot=0, cropie=0,
                      squash=0, fermento=0,
                      condensed_fermento=0):
    db = connectdb()
    cursor = db.cursor(buffered=True)
    
    
    if copper != 0:
        cursor.execute("UPDATE ComposterSpeed SET acquired_copper = ComposterSpeed.acquired_copper + %s WHERE id = %s",(copper, id))
    
    if tighly_tied_haybale != 0:
        cursor.execute("UPDATE ComposterSpeed SET acquired_tighly_tied_haybale = ComposterSpeed.acquired_tighly_tied_haybale + %s WHERE id = %s",(tighly_tied_haybale, id))
    
    if hay_bale != 0:
        cursor.execute("UPDATE ComposterSpeed SET acquired_hay_bale = ComposterSpeed.acquired_hay_bale + %s WHERE id = %s",(hay_bale, id))
    
    if ench_golden_carrot != 0:
        cursor.execute("UPDATE ComposterSpeed SET acquired_ench_golden_carrot = ComposterSpeed.acquired_ench_golden_carrot + %s WHERE id = %s",(ench_golden_carrot, id))
    
    if cropie != 0:
        cursor.execute("UPDATE ComposterSpeed SET acquired_cropie = ComposterSpeed.acquired_cropie + %s WHERE id = %s",(cropie, id))
    
    if squash != 0:
        cursor.execute("UPDATE ComposterSpeed SET acquired_squash = ComposterSpeed.acquired_squash + %s WHERE id = %s",(squash, id))
    
    if fermento != 0:
        cursor.execute("UPDATE ComposterSpeed SET acquired_fermento = ComposterSpeed.acquired_fermento + %s WHERE id = %s",(fermento, id))
    
    if condensed_fermento != 0:
        cursor.execute("UPDATE ComposterSpeed SET acquired_condensed_fermento = ComposterSpeed.acquired_condensed_fermento + %s WHERE id = %s",(condensed_fermento, id))
        
    db.commit()
    
    

def increaseCostReduction(id, copper=0,ench_brown_mushroom=0,
                          mutant_nether_wart=0, ench_brown_mushroom_block=0,
                          ench_red_mushroom_block=0, cropie=0, squash=0,
                          fermento=0, condensed_fermento=0):
    db = connectdb()
    cursor = db.cursor(buffered=True)
    
    
    if copper != 0:
        cursor.execute("UPDATE CostReduction SET acquired_copper = CostReduction.acquired_copper + %s WHERE id = %s",(copper, id))
    
    if ench_brown_mushroom != 0:
        cursor.execute("UPDATE CostReduction SET acquired_ench_brown_mushroom = CostReduction.acquired_ench_brown_mushroom + %s WHERE id = %s",(ench_brown_mushroom, id))
    
    if mutant_nether_wart != 0:
        cursor.execute("UPDATE CostReduction SET acquired_mutant_nether_wart = CostReduction.acquired_mutant_nether_wart + %s WHERE id = %s",(mutant_nether_wart, id))
    
    if ench_brown_mushroom_block != 0:
        cursor.execute("UPDATE CostReduction SET acquired_ench_brown_mushroom_block = CostReduction.acquired_ench_brown_mushroom_block + %s WHERE id = %s",(ench_brown_mushroom_block, id))
        
    if ench_red_mushroom_block != 0:
        cursor.execute("UPDATE CostReduction SET acquired_ench_red_mushroom_block = CostReduction.acquired_ench_red_mushroom_block + %s WHERE id = %s",(ench_red_mushroom_block, id))
    
    if cropie != 0:
        cursor.execute("UPDATE CostReduction SET acquired_cropie = CostReduction.acquired_cropie + %s WHERE id = %s",(cropie, id))
    
    if squash != 0:
        cursor.execute("UPDATE CostReduction SET acquired_squash = CostReduction.acquired_squash + %s WHERE id = %s",(squash, id))
    
    if fermento != 0:
        cursor.execute("UPDATE CostReduction SET acquired_fermento = CostReduction.acquired_fermento + %s WHERE id = %s",(fermento, id))
    
    if condensed_fermento != 0:
        cursor.execute("UPDATE CostReduction SET acquired_condensed_fermento = CostReduction.acquired_condensed_fermento + %s WHERE id = %s",(condensed_fermento, id))
        
    db.commit()
    
    
def increaseFuelCap(id, copper=0, ench_sugar_cane=0,
                    ench_melon_block=0, cropie=0,
                    squash=0, fermento=0,
                    condensed_fermento=0):
    db = connectdb()
    cursor = db.cursor(buffered=True)
    
    
    if copper != 0:
        cursor.execute("UPDATE FuelCap SET acquired_copper = FuelCap.acquired_copper + %s WHERE id = %s",(copper, id))
    
    if ench_sugar_cane != 0:
        cursor.execute("UPDATE FuelCap SET acquired_ench_sugar_cane = FuelCap.acquired_ench_sugar_cane + %s WHERE id = %s",(ench_sugar_cane, id))
    
    if ench_melon_block != 0:
        cursor.execute("UPDATE FuelCap SET acquired_ench_melon_block = FuelCap.acquired_ench_melon_block + %s WHERE id = %s",(ench_melon_block, id))
    
    if cropie != 0:
        cursor.execute("UPDATE FuelCap SET acquired_cropie = FuelCap.acquired_cropie + %s WHERE id = %s",(cropie, id))
    
    if squash != 0:
        cursor.execute("UPDATE FuelCap SET acquired_squash = FuelCap.acquired_squash + %s WHERE id = %s",(squash, id))
    
    if fermento != 0:
        cursor.execute("UPDATE FuelCap SET acquired_fermento = FuelCap.acquired_fermento + %s WHERE id = %s",(fermento, id))
    
    if condensed_fermento != 0:
        cursor.execute("UPDATE FuelCap SET acquired_condensed_fermento = FuelCap.acquired_condensed_fermento + %s WHERE id = %s",(condensed_fermento, id))
        
    db.commit()
    
    
def increaseMultiDrop(id, copper=0, ench_baked_potato=0,
                    ench_pumpkin=0, polished_pumpkin=0,
                    cropie=0, squash=0, fermento=0,
                    condensed_fermento=0):
    db = connectdb()
    cursor = db.cursor(buffered=True)
    
    
    if copper != 0:
        cursor.execute("UPDATE MultiDrop SET acquired_copper = MultiDrop.acquired_copper + %s WHERE id = %s",(copper, id))
    
    if ench_baked_potato != 0:
        cursor.execute("UPDATE MultiDrop SET acquired_ench_baked_potato = MultiDrop.acquired_ench_baked_potato + %s WHERE id = %s",(ench_baked_potato, id))
    
    if ench_pumpkin != 0:
        cursor.execute("UPDATE MultiDrop SET acquired_ench_pumpkin = MultiDrop.acquired_ench_pumpkin + %s WHERE id = %s",(ench_pumpkin, id))
        
    if polished_pumpkin != 0:
        cursor.execute("UPDATE MultiDrop SET acquired_polished_pumpkin = MultiDrop.acquired_polished_pumpkin + %s WHERE id = %s", (polished_pumpkin, id))
    
    if cropie != 0:
        cursor.execute("UPDATE MultiDrop SET acquired_cropie = MultiDrop.acquired_cropie + %s WHERE id = %s",(cropie, id))
    
    if squash != 0:
        cursor.execute("UPDATE MultiDrop SET acquired_squash = MultiDrop.acquired_squash + %s WHERE id = %s",(squash, id))
    
    if fermento != 0:
        cursor.execute("UPDATE MultiDrop SET acquired_fermento = MultiDrop.acquired_fermento + %s WHERE id = %s",(fermento, id))
    
    if condensed_fermento != 0:
        cursor.execute("UPDATE MultiDrop SET acquired_condensed_fermento = MultiDrop.acquired_condensed_fermento + %s WHERE id = %s",(condensed_fermento, id))
        
    db.commit()
    
    
def increaseOrganicMatterCap(id, copper=0, ench_cactus=0,
                            ench_cookie=0, cropie=0,
                            squash=0, fermento=0,
                            condensed_fermento=0):
    db = connectdb()
    cursor = db.cursor(buffered=True)
    
    
    if copper != 0:
        cursor.execute("UPDATE OrganicMatterCap SET acquired_copper = OrganicMatterCap.acquired_copper + %s WHERE id = %s",(copper, id))
    
    if ench_cactus != 0:
        cursor.execute("UPDATE OrganicMatterCap SET acquired_ench_cactus = OrganicMatterCap.acquired_ench_cactus + %s WHERE id = %s",(ench_cactus, id))
    
    if ench_cookie != 0:
        cursor.execute("UPDATE OrganicMatterCap SET acquired_ench_cookie = OrganicMatterCap.acquired_ench_cookie + %s WHERE id = %s",(ench_cookie, id))
        
    if cropie != 0:
        cursor.execute("UPDATE OrganicMatterCap SET acquired_cropie = OrganicMatterCap.acquired_cropie + %s WHERE id = %s",(cropie, id))
    
    if squash != 0:
        cursor.execute("UPDATE OrganicMatterCap SET acquired_squash = OrganicMatterCap.acquired_squash + %s WHERE id = %s",(squash, id))
    
    if fermento != 0:
        cursor.execute("UPDATE OrganicMatterCap SET acquired_fermento = OrganicMatterCap.acquired_fermento + %s WHERE id = %s",(fermento, id))
    
    if condensed_fermento != 0:
        cursor.execute("UPDATE OrganicMatterCap SET acquired_condensed_fermento = OrganicMatterCap.acquired_condensed_fermento + %s WHERE id = %s",(condensed_fermento, id))
        
    db.commit()