# This file implements the !roulette command
# !roulette generates a random Fit Roulette and outputs it to the selected channel
# This is used for memes

# Includes
import random   # Needed for random generation

wildcards = [
    "Overpropped", "RR"
]

tank_types = [
    "shield buffer ", "active shield ", "passive shield ", "active armor ", "armor buffer ", "hull "
]

roles = [
    "DPS ", "logi ", "EWAR ", "neuting ", "tackle "
]

hulls = [
    "Impairor", "Ibis", "Velator", "Reaper", "Executioner", "Tormenter", "Inquisitor", "Crucifier", "Punisher", "Magnate", "Condor", "Bantam", "Kestrel", "Griffin", "Merlin", "Heron", "Atron", "Navitas", "Tristan", "Maulus", "Incursus", "Imicus", "Slasher", "Burst", "Breacher", "Vigil", "Rifter", "Probe", "Coercer", "Dragoon", "Cormorant", "Corax", "Catalyst", "Algos", "Thrasher", "Talwar", "Arbitrator", "Augoror", "Omen", "Maller", "Blackbird", "Osprey", "Caracal", "Moa", "Celestis", "Exequeror", "Thorax", "Vexor", "Bellicose", "Scythe", "Stabber", "Rupture", "Prophecy", "Harbinger", "Oracle", "Ferox", "Drake", "Naga", "Brutix", "Myrmidon", "Talos", "Cyclone", "Hurricane", "Tornado", "Armageddon", "Apocalypse", "Abaddon", "Scorpion", "Raven", "Rokh", "Dominix", "Megathron", "Hyperion", "Typhoon", "Tempest", "Maelstrom", "Imperial Navy Slicer", "Crucifier Navy Issue", "Magnate Navy Issue", "Caldari Navy Hookbill", "Griffin Navy Issue", "Heron Navy Issue", "Federation Navy Comet", "Maulus Navy Issue", "Imicus Navy Issue", "Republic Fleet Firetail", "Vigil Fleet Issue", "Probe Fleet Issue", "Vengeance", "Retribution", "Hawk", "Harpy", "Ishkur", "Enyo", "Wolf", "Jaguar", "Anathema", "Purifier", "Manticore", "Buzzard", "Nemesis", "Helios", "Cheetah", "Hound", "Sentinel", "Kitsune", "Keres", "Hyena", "Crusader", "Malediction", "Crow", "Raptor", "Taranis", "Ares", "Claw", "Stiletto", "Deacon", "Kirin", "Thalia", "Scalpel", "Coercer Navy Issue", "Cormorant Navy Issue", "Catalyst Navy Issue", "Thrasher Fleet Issue", "Pontifex", "Stork", "Magus", "Bifrost", "Heretic", "Flycatcher", "Eris", "Sabre", "Confessor", "Jackdaw", "Hecate", "Svipul", "Augoror Navy Issue", "Omen Navy Issue", "Caracal Navy Issue", "Osprey Navy Issue", "Exequeror Navy Issue", "Vexor Navy Issue", "Scythe Fleet Issue", "Stabber Fleet Issue", "Zealot", "Sacrilege", "Eagle", "Cerberus", "Ishtar", "Deimos", "Vagabond", "Muninn", "Devoter", "Onyx", "Phobos", "Broadsword", "Guardian", "Basilisk", "Oneiros", "Scimitar", "Curse", "Pilgrim", "Falcon", "Rook", "Arazu", "Lachesis", "Huginn", "Rapier", "Legion", "Tengu", "Proteus", "Loki", "Harbinger Navy Issue", "Prophecy Navy Issue", "Drake Navy Issue", "Ferox Navy Issue", "Brutix Navy Issue", "Myrmidon Navy Issue", "Hurricane Fleet Issue", "Cyclone Fleet Issue", "Damnation", "Absolution", "Vulture", "Nighthawk", "Astarte", "Eos", "Claymore", "Sleipnir", "Apocalypse Navy Issue", "Armageddon Navy Issue", "Scorpion Navy Issue", "Raven Navy Issue", "Megathron Navy Issue", "Dominix Navy Issue", "Tempest Fleet Issue", "Typhoon Fleet Issue", "Redeemer", "Widow", "Sin", "Panther", "Paladin", "Golem", "Kronos", "Vargur", "Bestower", "Sigil", "Badger", "Tayra", "Nereus", "Kryos", "Epithal", "Miasmos", "Iteron Mark V", "Hoarder", "Mammoth", "Wreather", "Prorator", "Impel", "Crane", "Bustard", "Viator", "Occator", "Mastodon", "Prowler", "Venture", "Prospect", "Endurance", "Covetor", "Retriever", "Procurer", "Porpoise", "Damavik", "Nergal", "Kikimora", "Draugur", "Rodiva", "Vedmak", "Ikitursa", "Zarmazd", "Drekavac", "Leshak"
]

def spin():
    output_string = ""

    wildcard_count = random.randint(0,len(wildcards))

    wildcard_options = wildcards

    if wildcard_count > 0:
        for i in range(wildcard_count):
            wildcard_choice = random.choice(wildcard_options)

            output_string += wildcard_choice + " "
            wildcard_options.remove(wildcard_choice)
    
    output_string += random.choice(tank_types)# + "tank "

    output_string += random.choice(roles)

    output_string += random.choice(hulls)

    return output_string

print(spin())