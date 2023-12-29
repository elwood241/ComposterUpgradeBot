from discord.ext import commands
from discord import app_commands
import discord
import api

class TimeOut(discord.ui.View):
    def __init__(self, timeout = 180):
        super().__init__(timeout = timeout)
    
    async def on_timeout(self):
        if self.message:
            await self.message.edit(view=None)

    def setMessage(self, message):
        self.message = message
        
ids = [471036610561966111, 609454099427229736]
class increaseValueCommands(discord.app_commands.Group):
    @app_commands.command(name="composterspeedvalue", description="Increases the Value for ComposterSpeed Table")
    async def increaseComposterSpeedValue(self, ctx, id: int=7, copper: int=0,
                                    tighly_tied_haybale: int=0, hay_bale: int=0,
                                    ench_golden_carrot: int=0, cropie: int=0,
                                    squash: int=0, fermento: int=0,
                                    condensed_fermento: int=0):
        await ctx.response.defer()
        if not ctx.user.id in ids:
            await ctx.followup.send("DU GERAET EINES BAUMES (Du darfst das nicht!)")
            return
        api.increaseComposterSpeed(id=id, copper=copper,
                                   tighly_tied_haybale=tighly_tied_haybale,
                                   hay_bale=hay_bale, ench_golden_carrot=ench_golden_carrot,
                                   cropie=cropie, squash=squash, fermento=fermento,
                                   condensed_fermento=condensed_fermento)
        await ctx.followup.send("SUCCESS")
        
        
        
    @app_commands.command(name="costreductionvalue", description="Increases the Value for CostReduction Table")
    async def increaseCostReductionValue(self, ctx, id: int=7, copper: int=0,ench_brown_mushroom: int=0,
                                        mutant_nether_wart: int=0, ench_brown_mushroom_block: int=0,
                                        ench_red_mushroom_block: int=0, cropie: int=0, squash: int=0,
                                        fermento: int=0, condensed_fermento: int=0):
        await ctx.response.defer()
        if not ctx.user.id in ids:
            await ctx.followup.send("DU GERAET EINES BAUMES (Du darfst das nicht!)")
            return
        api.increaseCostReduction(id=id, copper=copper,
                                   ench_brown_mushroom=ench_brown_mushroom,
                                   mutant_nether_wart=mutant_nether_wart,
                                   ench_brown_mushroom_block=ench_brown_mushroom_block,
                                   ench_red_mushroom_block=ench_red_mushroom_block,
                                   cropie=cropie, squash=squash, fermento=fermento,
                                   condensed_fermento=condensed_fermento)
        await ctx.followup.send("SUCCESS")
        
        
        
    @app_commands.command(name="fuelcapvalue", description="Increases the Value for FuelCap Table")
    async def increaseFuelCapValue(self, ctx, id: int=7, copper: int=0, ench_sugar_cane: int=0,
                                   ench_melon_block: int=0, cropie: int=0, squash: int=0,
                                   fermento: int=0, condensed_fermento: int=0):
        await ctx.response.defer()
        if not ctx.user.id in ids:
            await ctx.followup.send("DU GERAET EINES BAUMES (Du darfst das nicht!)")
            return
        api.increaseFuelCap(id=id, copper=copper, ench_sugar_cane=ench_sugar_cane,
                            ench_melon_block=ench_melon_block, cropie=cropie,
                            squash=squash, fermento=fermento, condensed_fermento=condensed_fermento)
        await ctx.followup.send("SUCCESS")
        
        
        
    @app_commands.command(name="mulitdropvalue", description="Increases the Value for MultiDrop Table")
    async def increaseMultiDropValue(self, ctx, id: int=7, copper: int=0, ench_baked_potato: int=0,
                                    ench_pumpkin: int=0, polished_pumpkin: int=0,
                                    cropie: int=0, squash: int=0, fermento: int=0,
                                    condensed_fermento: int=0):
        await ctx.response.defer()
        if not ctx.user.id in ids:
            await ctx.followup.send("DU GERAET EINES BAUMES (Du darfst das nicht!)")
            return
        api.increaseMultiDrop(id=id, copper=copper, ench_baked_potato=ench_baked_potato,
                            ench_pumpkin=ench_pumpkin, polished_pumpkin=polished_pumpkin,
                            cropie=cropie, squash=squash, fermento=fermento,
                            condensed_fermento=condensed_fermento)
        await ctx.followup.send("SUCCESS")
        
        
        
    @app_commands.command(name="organicmattercapvalue", description="Increases the Value for OrganicMatterCap Table")
    async def increaseOrganicMatterCapValue(self, ctx, id: int=7, copper: int=0, ench_cactus: int=0,
                                   ench_cookie: int=0, cropie: int=0, squash: int=0,
                                   fermento: int=0, condensed_fermento: int=0):
        await ctx.response.defer()
        if not ctx.user.id in ids:
            await ctx.followup.send("DU GERAET EINES BAUMES (Du darfst das nicht!)")
            return
        api.increaseOrganicMatterCap(id=id, copper=copper, ench_cactus=ench_cactus,
                            ench_cookie=ench_cookie, cropie=cropie, squash=squash,
                            fermento=fermento, condensed_fermento=condensed_fermento)
        await ctx.followup.send("SUCCESS")
                            
        
        
        
class ComposterUpgradesCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
         
    
    @commands.Cog.listener()
    async def on_ready(self):
        increasecmds = increaseValueCommands(name="increase", description="Increase it")
        self.bot.tree.add_command(increasecmds)
    
    
    @app_commands.command(name="info", description="Get Some Infos")
    async def info(self, ctx, id: int=7):
        await ctx.response.defer()
        selectedButton = "speed"
        composterSpeedValues = api.getComposterSpeed(id)
        composterCostReductionValues = api.getCostReduction(id)
        composterFuelCapValues = api.getFuelCap(id)
        composterMultiDropValues = api.getMultiDrop(id)
        composterOrganicMatterCap = api.getOrganicMatterCap(id)
        
        def generateProgress(name: str, acquired: int, required: int):
            return f"\n### {name}\n`{acquired} / {required}` - `{required - acquired} missing` ({acquired / required * 100:.2f}%)" if acquired < required else f"\n### {name}\n`{acquired} / {required}` You are Done 🍪"
            
        def generateProgressBar(progress):
            bar_length = 15
            filled_length = int(round(bar_length * progress))
            green_box = '🟩'
            grey_box = '⬛'
            emoji_bar = [green_box] * filled_length + [grey_box] * (bar_length - filled_length)
            return "\n" + ''.join(emoji_bar)
        
        def generateView():
            
            speedValuesButton = discord.ui.Button(label="ComposterSpeed", style=discord.ButtonStyle.green if selectedButton=="speed" else discord.ButtonStyle.blurple)
            cdrValuesButton = discord.ui.Button(label="CostReduction", style=discord.ButtonStyle.green if selectedButton=="reduction" else discord.ButtonStyle.blurple)
            fuelValuesButton = discord.ui.Button(label="FuelCap", style=discord.ButtonStyle.green if selectedButton=="fuel" else discord.ButtonStyle.blurple)
            multidropValuesButton = discord.ui.Button(label="MultiDrop", style=discord.ButtonStyle.green if selectedButton=="multidrop" else discord.ButtonStyle.blurple)
            organicmatterValuesButoon = discord.ui.Button(label="OrganicMatterCap", style=discord.ButtonStyle.green if selectedButton=="organic" else discord.ButtonStyle.blurple)  
            
            speedValuesButton.callback=speedValuesCallback
            cdrValuesButton.callback=cRValuesCallback
            fuelValuesButton.callback=fuelValuesCallback
            multidropValuesButton.callback=multiDropValuesCallback
            organicmatterValuesButoon.callback=organicMatterValuesCallback
            
            view = TimeOut()
            view.add_item(speedValuesButton)
            view.add_item(cdrValuesButton)
            view.add_item(fuelValuesButton)
            view.add_item(multidropValuesButton)
            view.add_item(organicmatterValuesButoon)
            return view
                        
        def generateSpeedValuesEmbeddescription():
            generatedDescription = "# ComposterSpeed\n"
            nonlocal selectedButton
            nonlocal composterSpeedValues
            selectedButton = "speed"
            generatedDescription += generateProgress("Copper", composterSpeedValues[9], composterSpeedValues[1])
            generatedDescription += generateProgressBar(composterSpeedValues[9] / composterSpeedValues[1])
            
            generatedDescription += generateProgress("Tightly Tied Haybale", composterSpeedValues[10], composterSpeedValues[2])
            generatedDescription += generateProgressBar(composterSpeedValues[10] / composterSpeedValues[2])
            
            generatedDescription += generateProgress("Haybale", composterSpeedValues[11], composterSpeedValues[3])
            generatedDescription += generateProgressBar(composterSpeedValues[11] / composterSpeedValues[3])
            
            generatedDescription += generateProgress("Enchanted Golden Carrot", composterSpeedValues[12], composterSpeedValues[4])
            generatedDescription += generateProgressBar(composterSpeedValues[12] / composterSpeedValues[4])
            
            generatedDescription += generateProgress("Cropie", composterSpeedValues[13], composterSpeedValues[5])
            generatedDescription += generateProgressBar(composterSpeedValues[13] / composterSpeedValues[5])
            
            generatedDescription += generateProgress("Squash", composterSpeedValues[14], composterSpeedValues[6])
            generatedDescription += generateProgressBar(composterSpeedValues[14] / composterSpeedValues[6])
            
            generatedDescription += generateProgress("Fermento", composterSpeedValues[15], composterSpeedValues[7])
            generatedDescription += generateProgressBar(composterSpeedValues[15] / composterSpeedValues[7])
            
            generatedDescription += generateProgress("Condensed Fermento", composterSpeedValues[16], composterSpeedValues[8])
            generatedDescription += generateProgressBar(composterSpeedValues[16] / composterSpeedValues[8])
            return generatedDescription
        
        async def speedValuesCallback(interaction: discord.interactions):
            composterOverviewEmbed=discord.Embed(
                title="ComposterUpgrades Overview",
                description=generateSpeedValuesEmbeddescription(),
                color=0xff8b19, 
            )
            view=generateView()
            message = await interaction.response.edit_message(embed=composterOverviewEmbed, view=view)
            view.setMessage(message)
            
            
        def generateCRValuesEmbeddescription():
            generatedDescription = "# CostReduction\n"
            nonlocal selectedButton
            nonlocal composterCostReductionValues
            selectedButton = "reduction"
            generatedDescription += generateProgress("Copper", composterCostReductionValues[10], composterCostReductionValues[1])
            generatedDescription += generateProgressBar(composterCostReductionValues[10] / composterCostReductionValues[1])
            
            generatedDescription += generateProgress("Enchanted Brown Mushroom", composterCostReductionValues[11], composterCostReductionValues[2])
            generatedDescription += generateProgressBar(composterCostReductionValues[11] / composterCostReductionValues[2])
            
            generatedDescription += generateProgress("Mutant Nether Wart", composterCostReductionValues[12], composterCostReductionValues[3])
            generatedDescription += generateProgressBar(composterCostReductionValues[12] / composterCostReductionValues[3])
            
            generatedDescription += generateProgress("Enchanted Brown Mushroom Block", composterCostReductionValues[13], composterCostReductionValues[4])
            generatedDescription += generateProgressBar(composterCostReductionValues[13] / composterCostReductionValues[4])
            
            generatedDescription += generateProgress("Enchanted Red Mushroom Block", composterCostReductionValues[14], composterCostReductionValues[5])
            generatedDescription += generateProgressBar(composterCostReductionValues[14] / composterCostReductionValues[5])
            
            generatedDescription += generateProgress("Cropie", composterCostReductionValues[15], composterCostReductionValues[6])
            generatedDescription += generateProgressBar(composterCostReductionValues[15] / composterCostReductionValues[6])
            
            generatedDescription += generateProgress("Squash", composterCostReductionValues[16], composterCostReductionValues[7])
            generatedDescription += generateProgressBar(composterCostReductionValues[16] / composterCostReductionValues[7])
            
            generatedDescription += generateProgress("Fermento", composterCostReductionValues[17], composterCostReductionValues[8])
            generatedDescription += generateProgressBar(composterCostReductionValues[17] / composterCostReductionValues[8])
            
            generatedDescription += generateProgress("Condensed Fermento", composterCostReductionValues[18], composterCostReductionValues[9])
            generatedDescription += generateProgressBar(composterCostReductionValues[18] / composterCostReductionValues[9])
            return generatedDescription
        
        async def cRValuesCallback(interaction):
            composterOverviewEmbed=discord.Embed(
                title="ComposterUpgrades Overview",
                description=generateCRValuesEmbeddescription(),
                color=0xff8b19, 
            )
            view=generateView()
            message = await interaction.response.edit_message(embed=composterOverviewEmbed, view=view)
            view.setMessage(message)
            
            
        def generateFuelValuesEmbeddescription():
            generatedDescription = "# FuelCap\n"
            nonlocal selectedButton
            nonlocal composterFuelCapValues
            selectedButton = "fuel"
            generatedDescription += generateProgress("Copper", composterFuelCapValues[8], composterFuelCapValues[1])
            generatedDescription += generateProgressBar(composterFuelCapValues[8] / composterFuelCapValues[1])

            generatedDescription += generateProgress("Enchanted Cactus", composterFuelCapValues[9], composterFuelCapValues[2])
            generatedDescription += generateProgressBar(composterFuelCapValues[9] / composterFuelCapValues[2])

            generatedDescription += generateProgress("Enchanted Sugar Cane", composterFuelCapValues[10], composterFuelCapValues[3])
            generatedDescription += generateProgressBar(composterFuelCapValues[10] / composterFuelCapValues[3])
            
            generatedDescription += generateProgress("Cropie", composterFuelCapValues[11], composterFuelCapValues[4])
            generatedDescription += generateProgressBar(composterFuelCapValues[11] / composterFuelCapValues[4])
            
            generatedDescription += generateProgress("Squash", composterFuelCapValues[12], composterFuelCapValues[5])
            generatedDescription += generateProgressBar(composterFuelCapValues[12] / composterFuelCapValues[5])
            
            generatedDescription += generateProgress("Fermento", composterFuelCapValues[13], composterFuelCapValues[6])
            generatedDescription += generateProgressBar(composterFuelCapValues[13] / composterFuelCapValues[6])
            
            generatedDescription += generateProgress("Condensed Fermento", composterFuelCapValues[14], composterFuelCapValues[7])
            generatedDescription += generateProgressBar(composterFuelCapValues[14] / composterFuelCapValues[7])
            return generatedDescription
        
        async def fuelValuesCallback(interaction):
            composterOverviewEmbed=discord.Embed(
                title="ComposterUpgrades Overview",
                description=generateFuelValuesEmbeddescription(),
                color=0xff8b19, 
            )
            view=generateView()
            message = await interaction.response.edit_message(embed=composterOverviewEmbed, view=view)
            view.setMessage(message)
            
            
        def generateMultiDropValuesEmbeddescription():
            generatedDescription = "# MultiDrop\n"
            nonlocal selectedButton
            nonlocal composterMultiDropValues
            selectedButton = "multidrop"
            generatedDescription += generateProgress("Copper", composterOrganicMatterCap[9], composterOrganicMatterCap[1])
            generatedDescription += generateProgressBar(composterMultiDropValues[9] / composterMultiDropValues[1])
            
            generatedDescription += generateProgress("Enchanted Bake Potato", composterMultiDropValues[10], composterMultiDropValues[2])
            generatedDescription += generateProgressBar(composterMultiDropValues[10] / composterMultiDropValues[2])
            
            generatedDescription += generateProgress("Enchanted Pumpkin", composterMultiDropValues[11], composterMultiDropValues[3])
            generatedDescription += generateProgressBar(composterMultiDropValues[11] / composterMultiDropValues[3])
            
            generatedDescription += generateProgress("Polished Pumpkin", composterMultiDropValues[12], composterMultiDropValues[4])
            generatedDescription += generateProgressBar(composterMultiDropValues[12] / composterMultiDropValues[4])
            
            generatedDescription += generateProgress("Cropie", composterMultiDropValues[13], composterMultiDropValues[5])
            generatedDescription += generateProgressBar(composterMultiDropValues[13] / composterMultiDropValues[5])
            
            generatedDescription += generateProgress("Squash", composterMultiDropValues[14], composterMultiDropValues[6])
            generatedDescription += generateProgressBar(composterMultiDropValues[14] / composterMultiDropValues[6])
            
            generatedDescription += generateProgress("Fermento", composterMultiDropValues[15], composterMultiDropValues[7])
            generatedDescription += generateProgressBar(composterMultiDropValues[15] / composterMultiDropValues[7])
            
            generatedDescription += generateProgress("Condensed Fermento", composterMultiDropValues[16], composterMultiDropValues[8])
            generatedDescription += generateProgressBar(composterMultiDropValues[16] / composterMultiDropValues[8])
            return generatedDescription
        
        async def multiDropValuesCallback(interaction):
            composterOverviewEmbed=discord.Embed(
                title="ComposterUpgrades Overview",
                description=generateMultiDropValuesEmbeddescription(),
                color=0xff8b19, 
            )
            view=generateView()
            message = await interaction.response.edit_message(embed=composterOverviewEmbed, view=view)
            view.setMessage(message)
            
            
        def generateOrganicMatterValuesEmbeddescription():
            generatedDescription = "# OrganicMatterCap\n"
            nonlocal selectedButton
            nonlocal composterOrganicMatterCap
            selectedButton = "organic"
            generatedDescription += generateProgress("Copper", composterOrganicMatterCap[8], composterOrganicMatterCap[1])
            generatedDescription += generateProgressBar(composterOrganicMatterCap[8] / composterOrganicMatterCap[1])
            
            generatedDescription += generateProgress("Enchanted Cactus", composterOrganicMatterCap[9], composterOrganicMatterCap[2])
            generatedDescription += generateProgressBar(composterOrganicMatterCap[9] / composterOrganicMatterCap[2])
            
            generatedDescription += generateProgress("Enchanted Cookie", composterOrganicMatterCap[10], composterOrganicMatterCap[3])
            generatedDescription += generateProgressBar(composterOrganicMatterCap[10] / composterOrganicMatterCap[3])
            
            generatedDescription += generateProgress("Cropie", composterOrganicMatterCap[11], composterOrganicMatterCap[4])
            generatedDescription += generateProgressBar(composterOrganicMatterCap[11] / composterOrganicMatterCap[4])
            
            generatedDescription += generateProgress("Squash", composterOrganicMatterCap[12], composterOrganicMatterCap[5])
            generatedDescription += generateProgressBar(composterOrganicMatterCap[12] / composterOrganicMatterCap[5])
            
            generatedDescription += generateProgress("Fermento", composterOrganicMatterCap[13], composterOrganicMatterCap[6])
            generatedDescription += generateProgressBar(composterOrganicMatterCap[13] / composterOrganicMatterCap[6])
            
            generatedDescription += generateProgress("Condensed Fermento", composterOrganicMatterCap[14], composterOrganicMatterCap[7])
            generatedDescription += generateProgressBar(composterOrganicMatterCap[14] / composterOrganicMatterCap[7])
            return generatedDescription
        
        async def organicMatterValuesCallback(interaction):
            composterOverviewEmbed=discord.Embed(
                title="ComposterUpgrades Overview",
                description=generateOrganicMatterValuesEmbeddescription(),
                color=0xff8b19, 
            )
            view=generateView()
            message = await interaction.response.edit_message(embed=composterOverviewEmbed, view=view)
            view.setMessage(message)
        
            
            
            
            
            
            
            
            
        composterOverviewEmbed=discord.Embed(
                title="ComposterUpgrades Overview",
                description=generateSpeedValuesEmbeddescription(),
                color=0xff8b19, 
            )

        view=generateView()
        message = await ctx.followup.send(embed=composterOverviewEmbed, view=view)
        view.setMessage(message)
        
        
        
    
    
async def setup(bot):
    await bot.add_cog(ComposterUpgradesCommands(bot))