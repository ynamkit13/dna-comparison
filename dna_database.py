"""
COI (Cytochrome c Oxidase Subunit I) Barcode DNA Sequence Database

Contains 34 real COI-5P barcode sequences from NCBI GenBank, covering:
  - 7 Mammals
  - 7 Birds
  - 6 Fish
  - 6 Insects
  - 5 Reptiles
  - 3 Amphibians

Each sequence is a ~200bp fragment from the 5' end of the COI gene.
All sequences were retrieved from NCBI GenBank (https://www.ncbi.nlm.nih.gov/).
Accession numbers are provided for verification.
"""


COI_DATABASE = [
    # === Mammals (7 species) ===
    {
        "species": "Homo sapiens",
        "common_name": "Human",
        "group": "Mammals",
        "gene": "COI",
        "accession": "PV276824.1",
        "sequence": "TATTCGGCGCATGAGCTGGAGTCCTAGGCACAGCTCTAAGCCTCCTTATTCGAGCCGAGCTGGGCCAGCCAGGCAACCTTCTAGGTAACGACCACATCTACAACGTTATCGTCACAGCCCATGCATTTGTAATAATCTTCTTCATAGTAATACCCATCATAATCGGAGGCTTTGGCAACTGACTAGTTCCCCTAATAATC",
    },
    {
        "species": "Canis lupus familiaris",
        "common_name": "Dog",
        "group": "Mammals",
        "gene": "COI",
        "accession": "PV639633.1",
        "sequence": "GGGGCTTTGGAAACTGACTAGTGCCGTTAATAATTGGTGCTCCGGACATGGCATTCCCCCGAATAAATAACATGAGCTTCTGACTCCTTCCTCCATCCTTTCTTCTACTATTAGCATCTTCTATGGTAGAAGCAGGTGCAGGAACGGGATGAACCGTATACCCCCCACTGGCTGGCAATCTGGCCCATGCAGGAGCATCC",
    },
    {
        "species": "Felis catus",
        "common_name": "Cat",
        "group": "Mammals",
        "gene": "COI",
        "accession": "PV639086.1",
        "sequence": "AACACTATATTACTAACAGATCGAAACCTAAACACCACATTCTTTGACCCCGCTGGGGGAGGAGATCCTATCTTATACCAACACTTATTCTGATTCTTTGGCCATCCAGAAGTTTACATTTTAATCCTACCCGGTTTTGGGGTAATCTCACATATTGTTACCTACTACTCAGGTAAAAAAGAACCCTTTGGCTACATGGG",
    },
    {
        "species": "Bos taurus",
        "common_name": "Cow",
        "group": "Mammals",
        "gene": "COI",
        "accession": "KP777007.1",
        "sequence": "GCTCAGCCATTTTACCCATGTTCATTAACCGCTGACTATTCTCAACTAACCATAAAGATATTGGTACCCTTTATCTACTATTTGGTGCTTGGGCCGGTATAGTAGGAACAGCTCTAAGCCTTCTAATTCGCGCTGAATTAGGCCAACCCGGAACTCTGCTCGGAGACGACCAAATCTACAACGTAGTTGTAACCGCACAC",
    },
    {
        "species": "Equus caballus",
        "common_name": "Horse",
        "group": "Mammals",
        "gene": "COI",
        "accession": "PV786437.1",
        "sequence": "GAGCTGGAATAGTAGGAACTGCCCTAAGCCTCCTAATCCGTGCTGAATTAGGCCAACCTGGGACCCTACTAGGAGATGATCAGATCTACAATGTTATTGTAACCGCCCATGCATTCGTAATAATTTTCTTTATGGTCATACCCATTATAATCGGAGGATTCGGAAACTGATTAGTCCCCCTGATAATTGGAGCACCTGAT",
    },
    {
        "species": "Tursiops truncatus",
        "common_name": "Bottlenose Dolphin",
        "group": "Mammals",
        "gene": "COI",
        "accession": "OR934709.1",
        "sequence": "CTTTATAGTTATACCTATCATAATTGGAGGTTTTGGGAACTGGTTAGTCCCCTTAATAATCGGAGCTCCTGACATAGCATTCCCCCGTCTAAACAACATAAGCTTCTGACTACTCCCCCCTTCCTTTCTACTACTAATAGCATCTTCAATAATTGAGGCCGGCGCAGGTACAGGCTGAACTGTTTACCCTCCTCTAGCTG",
    },
    {
        "species": "Myotis lucifugus",
        "common_name": "Little Brown Bat",
        "group": "Mammals",
        "gene": "COI",
        "accession": "PX671444.1",
        "sequence": "TTTCTTCATAGTTATACCTATTATAATCGGGGGGTTCGGAAATTGATTAGTGCCCTTAATAATTGGCGCCCCTGATATAGCTTTCCCTCGAATAAATAACATAAGCTTTTGACTACTCCCCCCATCTTTTCTATTACTGCTGGCCTCATCTATAGTTGAAGCGGGAGCAGGCACTGGTTGGACAGTATACCCCCCTCTAG",
    },

    # === Birds (7 species) ===
    {
        "species": "Gallus gallus",
        "common_name": "Chicken",
        "group": "Birds",
        "gene": "COI",
        "accession": "KY264686.1",
        "sequence": "GCCGGCACAGCACTTAGCCTTCTAATTCGCGCAGAACTAGGACAGCCCGGAACTCTCTTAGGAGACGATCAAATTTACAATGTAATCGTCACAGCCCATGCTTTCGTCATAATCTTCTTTATAGTTATACCCATCATGATCGGTGGCTTCGGAAACTGACTAGTCCCGCTTATAATCGGTGCCCCAGACATAGCATTCCC",
    },
    {
        "species": "Aquila chrysaetos",
        "common_name": "Golden Eagle",
        "group": "Birds",
        "gene": "COI",
        "accession": "AY666481.1",
        "sequence": "CCGCCCTTAGCCTTCTTATCCGCGCAGAACTTGGCCAACCTGGCACCCTCTTAGGCGATGACCAAATCTACAATGTAATCGTCACCGCTCATGCTTTCGTAATAATCTTCTTCATAGTCATACCAATCATAATTGGAGGCTTTGGAAACTGACTTGTCCCACTCATAATTGGCGCCCCCGACATAGCCTTCCCACGCATA",
    },
    {
        "species": "Aptenodytes forsteri",
        "common_name": "Emperor Penguin",
        "group": "Birds",
        "gene": "COI",
        "accession": "EU525299.1",
        "sequence": "GTGACATTCATTAACCGATGACTATTCTCAACAAACCACAAAGATATCGGCACCCTTTACCTAATTTTCGGTGCATGAGCAGGCATGGCCGGAACCGCCCTCAGCCTGCTTATTCGTGCAGAACTCGGCCAGCCAGGAACCCTCCTAGGAGACGACCAAATCTACAACGTAATCGTCACCGCCCACGCCTTCGTAATAAT",
    },
    {
        "species": "Passer domesticus",
        "common_name": "House Sparrow",
        "group": "Birds",
        "gene": "COI",
        "accession": "PV835582.1",
        "sequence": "AAAGACATTGGCACCCTGTACCTAATCTTCGGCGCATGAGCCGGGATGGTAGGTACCGCCCTAAGCTTACTTATCCGAGCAGAACTTGGACAACCAGGGGCTCTCCTAGGAGATGACCAAGTTTACAACGTAGTTGTCACAGCCCATGCTTTCGTGATAATCTTCTTCATAGTTATGCCAATTATAATTGGGGGATTCGG",
    },
    {
        "species": "Bubo bubo",
        "common_name": "Eurasian Eagle-Owl",
        "group": "Birds",
        "gene": "COI",
        "accession": "KY754487.1",
        "sequence": "CCTCTACCTAATCTTCGGGGCATGAGCAGGCATAGTTGGCACTGCCCTCAGCCTACTTATCCGAGCCGAACTCGGCCAACCCGGGACCCTTCTTGGCGACGACCAAATCTACAACGTAGTTGTCACCGCCCATGCCTTTGTAATAATCTTTTTTATGGTCATACCCATCATGATCGGAGGATTTGGAAACTGATTAGTCC",
    },
    {
        "species": "Melopsittacus undulatus",
        "common_name": "Budgerigar",
        "group": "Birds",
        "gene": "COI",
        "accession": "MN737013.1",
        "sequence": "TCTTCGGTGCATGAGCCGGCATAATCGGCACCGCCCTAAGCCTACTCATTCGAGCAGAACTAGGCCAACCAGGAACCCTACTAGGAGACGACCAAATCTATAACGTAATCGTCACCGCCCATGCCTTCGTAATAATCTTCTTCATAGTAATACCAATCATAATCGGAGGATTTGGAAACTGACTAGTCCCCCTCATAATT",
    },
    {
        "species": "Corvus corax",
        "common_name": "Common Raven",
        "group": "Birds",
        "gene": "COI",
        "accession": "GQ481624.1",
        "sequence": "TCTGTACCTAATCTTCGGAGCATGAGCCGGAATAGTAGGTACCGCCCTAAGTCTCCTTATCCGAGCAGAACTAGGCCAACCAGGCGCTCTGCTAGGAGACGACCAAATCTACAATGTAATCGTTACAGCTCACGCTTTCGTTATAATCTTCTTCATAGTTATACCAATCATAATCGGGGGATTTGGAAACTGACTAGTTC",
    },

    # === Fish (6 species) ===
    {
        "species": "Salmo salar",
        "common_name": "Atlantic Salmon",
        "group": "Fish",
        "gene": "COI",
        "accession": "PV570336.1",
        "sequence": "ATAGTCGGCACCGCCCTAAGTCTCTTGATTCGAGCAGAACTCAGCCAGCCTGGCGCCCTTCTGGGAGATGACCAAATTTATAACGTAATTGTTACAGCCCATGCCTTCGTCATAATTTTCTTTATAGTCATACCGATTATGATCGGCGGCTTTGGAAACTGATTAATTCCTCTTATAATCGGGGCCCCCGACATAGCATT",
    },
    {
        "species": "Thunnus albacares",
        "common_name": "Yellowfin Tuna",
        "group": "Fish",
        "gene": "COI",
        "accession": "PX552217.1",
        "sequence": "ACGACCAGATCTACAATGTAATCGTTACGGCCCATGCCTTCGTAATGATTTTCTTTATAGTAATACCAATTATGATTGGAGGATTTGGAAACTGACTTATTCCTCTAATGATCGGAGCCCCCGACATGGCATTCCCACGAATGAACAACATGAGCTTCTGACTCCTTCCCCCCTCTTTCCTTCTGCTCCTAGCTTCTTCA",
    },
    {
        "species": "Danio rerio",
        "common_name": "Zebrafish",
        "group": "Fish",
        "gene": "COI",
        "accession": "PZ234837.1",
        "sequence": "GGAACTGCATTAAGCCTTTTAATCCGAGCCGAACTTAGCCAACCAGGAGCACTCCTTGGTGATGATCAAATTTATAATGTTATTGTTACTGCCCATGCTTTTGTAATAATTTTCTTTATAGTAATACCCATTCTTATTGGGGGGTTTGGAAACTGACTTGTGCCACTAATGATTGGAGCCCCCGATATGGCGTTTCCGCG",
    },
    {
        "species": "Gadus morhua",
        "common_name": "Atlantic Cod",
        "group": "Fish",
        "gene": "COI",
        "accession": "PV541600.1",
        "sequence": "TAGTCGGAACAGCCCTAAGCCTGCTCATTCGAGCAGAGCTAAGTCAACCTGGTGCACTTCTTGGTGATGATCAAATTTATAATGTGATCGTTACAGCGCACGCTTTCGTAATAATTTTCTTTATAGTAATACCACTAATAATTGGAGGCTTTGGGAACTGACTCATTCCTCTAATGATCGGTGCACCAGATATAGCTTTC",
    },
    {
        "species": "Carcharodon carcharias",
        "common_name": "Great White Shark",
        "group": "Fish",
        "gene": "COI",
        "accession": "KY909355.1",
        "sequence": "AGCCCTAAGCCTTTTAATCCGTGCCGAGCTGGGTCAACCAGGTTCCCTCCTCGGAGATGACCAGATTTATAATGTTATTGTGACCGCCCATGCCTTCGTAATAATCTTCTTCATGGTAATGCCCATCATAATTGGGGGTTTTGGGAATTGACTAATCCCATTAATAATTGGTGCCCCGGACATAGCCTTCCCCCGAATAA",
    },
    {
        "species": "Hippocampus kuda",
        "common_name": "Spotted Seahorse",
        "group": "Fish",
        "gene": "COI",
        "accession": "MW387359.1",
        "sequence": "CACCCTATACTTAGTATTTGGTGCTTGAGCCGGAATAGTCGGCACTGCACTCAGCCTTTTAATTCGAGCAGAACTAAGTCAGCCAGGAGCTTTACTAGGGGATGATCAAATCTATAATGTTATCGTAACTGCTCATGCTTTCGTAATAATTTTCTTTATAGTTATGCCTATCATAATTGGGGGTTTTGGTAATTGACTGG",
    },

    # === Insects (6 species) ===
    {
        "species": "Apis mellifera",
        "common_name": "Honeybee",
        "group": "Insects",
        "gene": "COI",
        "accession": "PZ160266.1",
        "sequence": "TTATTCGAATAGAATTAAGATCCCCAGGATCATGAATTAGCAATGATCAAATTTATAATACAATTGTTACTAGTCATGCATTCCTAATAATTTTTTTTATAGTTATACCATTTTTAATTGGAGGATTTGGAAATTGGCTTATTCCTTTAATACTAGGATCACCTGATATAGCATTCCCCCGAATAAATAATATTAGATTT",
    },
    {
        "species": "Drosophila melanogaster",
        "common_name": "Fruit Fly",
        "group": "Insects",
        "gene": "COI",
        "accession": "PX936386.1",
        "sequence": "AACTTTATATTTTATTTTTGGAGCTTGAGCTGGAATAGTTGGAACATCTTTAAGAATTTTAATTCGAGCTGAATTAGGACATCCTGGAGCATTAATTGGAGATGATCAAATTTATAATGTAATTGTAACTGCACATGCTTTTATTATAATTTTTTTTATAGTTATACCTATTATAATTGGTGGATTTGGAAATTGATTAG",
    },
    {
        "species": "Danaus plexippus",
        "common_name": "Monarch Butterfly",
        "group": "Insects",
        "gene": "COI",
        "accession": "OP587026.1",
        "sequence": "TACTTTATATTTTATTTTTGGAATTTGAGCAGGAATAGTTGGGACATCTTTAAGTCTTTTAATTCGAACAGAATTAGGAACTCCTGGATCTTTAATTGGTGATGATCAAATTTATAATACTATTGTTACAGCTCATGCTTTTATTATAATTTTTTTTATAGTTATACCAATTATAATTGGAGGATTTGGTAATTGATTAG",
    },
    {
        "species": "Aedes aegypti",
        "common_name": "Yellow Fever Mosquito",
        "group": "Insects",
        "gene": "COI",
        "accession": "PZ072287.1",
        "sequence": "ATTAGGAGCCCCTGATATAGCCTTTCCTCGAATAAATAATATAAGTTTTTGAATACTTCCTCCTTCATTGACTCTTCTATTATCAAGCTCAATAGTAGAAAATGGGGCAGGAACTGGGTGAACAGTTTATCCTCCTCTCTCTTCAGGAACAGCTCATGCTGGAGCTTCTGTTGATTTAGCTATTTTTTCTCTTCATTTAG",
    },
    {
        "species": "Bombyx mori",
        "common_name": "Silkworm Moth",
        "group": "Insects",
        "gene": "COI",
        "accession": "PX558639.1",
        "sequence": "TTTTATTTTTGGTATTTGATCAGGAATAATTGGAACATCTTTAAGACTTTTAATTCGAGCTGAATTAGGAAATCCAGGATCATTAATTGGAGATGATCAAATTTATAATACTATTGTAACAGCACATGCTTTTATTATAATTTTTTTTATAGTTATACCTATTATAATTGGAGGATTTGGAAATTGATTAGTTCCTCTTA",
    },
    {
        "species": "Acheta domesticus",
        "common_name": "House Cricket",
        "group": "Insects",
        "gene": "COI",
        "accession": "PX558714.1",
        "sequence": "CTTCATTTTCGGAGCTTGAGCTGGAATAGTAGGTACCTCTTTAAGTATCTTAATTCGAACGGAACTAGGACAACCAGGTTATTTAATTGGAGATGATCAAACATATAATGTTATCGTAACTGCACATGCATTTGTCATAATTTTTTTCATGGTTATACCAATTATAATTGGTGGATTCGGAAATTGATTAGTACCCCTAA",
    },

    # === Reptiles (5 species) ===
    {
        "species": "Chelonia mydas",
        "common_name": "Green Sea Turtle",
        "group": "Reptiles",
        "gene": "COI",
        "accession": "PX218923.1",
        "sequence": "GGATAGTCGGCACAGCACTCAGTTTATTAATCCGCGCAGAACTAAGCCAACCAGGAACTCTTCTAGGAGATGACCAAATCTATAATGTCATCGTTACAGCTCATGCCTTTATTATAATCTTCTTCATAGTTATACCAATTATAATTGGTGGCTTCGGAAATTGACTTGTTCCCCTAATAATTGGCGCACCAGACATAGCA",
    },
    {
        "species": "Python bivittatus",
        "common_name": "Burmese Python",
        "group": "Reptiles",
        "gene": "COI",
        "accession": "PP556868.1",
        "sequence": "TTGTAGGCGCCTGTTTAAGCGTATTAATACGAATAGAACTAACACAACCAGGCTCTTTATTCGGCAGCGACCAAATCTTTAATGTGCTTGTAACAGCCCACGCATTCGTAATAATTTTTTTTATAGTTATACCCATTATGATCGGAGGTTTCGGAAACTGATTAATCCCATTAATAATCGGAGCACCAGACATAGCATTC",
    },
    {
        "species": "Crocodylus niloticus",
        "common_name": "Nile Crocodile",
        "group": "Reptiles",
        "gene": "COI",
        "accession": "PP593431.1",
        "sequence": "CACCTTGTATTTTATTTTCGGCGCCTGAGCCGGAATAGTAGGCACAGCCATAAGCCTATTAATCCGAACAGAGCTCAGCCAGCCAGGCCCCTTCATAGGAGATGACCAAATTTACAATGTTATTGTTACAGCACATGCCTTTATCATAATTTTCTTTATAGTTATACCAATTATGATCGGAGGATTTGGAAATTGACTAC",
    },
    {
        "species": "Gekko gecko",
        "common_name": "Tokay Gecko",
        "group": "Reptiles",
        "gene": "COI",
        "accession": "MT608194.1",
        "sequence": "CACCCTATATTTTCTATTTGGTCTCTGAGCAGGCATAGTGGGCACAGCACTTAGCCTTCTTATCCGTGCTGAACTAAGTCAACCAGGGGCACTCCTTGGAAACGATCAACTATATAATGTAATCGTAACAGCACACGCATTTGTAATAATTTTCTTCATAGTGATACCTGTTATAATTGGGGGGTTTGGCAACTGATTAA",
    },
    {
        "species": "Iguana iguana",
        "common_name": "Green Iguana",
        "group": "Reptiles",
        "gene": "COI",
        "accession": "NC_002793.1",
        "sequence": "GTGTCAATCACCCGTTGATTCTTCTCAACCAACCACAAAGATATCGGCACCCTTTACTTAGTCTTCGGTGCCTGAGCCGGCATGGTCGGAACTGCCCTCAGCCTGCTAATTCGAGCAGAACTTAGCCAACCAGGGGCCCTTCTCGGCGACGACCAAATTTACAACGTTATTGTAACCGCCCATGCTTTTGTTATAATTTT",
    },

    # === Amphibians (3 species) ===
    {
        "species": "Xenopus laevis",
        "common_name": "African Clawed Frog",
        "group": "Amphibians",
        "gene": "COI",
        "accession": "OQ261767.1",
        "sequence": "CCTTTACTTAGTTTTTGGTGCTTGAGCAGGGATGGTCGGAACCGCTCTTAGCTTATTAATTCGAGCTGAACTTAGCCAGCCCGGAACACTACTTGGAGATGACCAAATTTATAATGTTATCGTTACAGCACATGCTTTTATTATAATTTTCTTCATAGTCATGCCTATTATAATCGGTGGATTTGGGAACTGATTAGTTC",
    },
    {
        "species": "Ambystoma mexicanum",
        "common_name": "Axolotl",
        "group": "Amphibians",
        "gene": "COI",
        "accession": "OK605097.1",
        "sequence": "CAGTTTCAACTAATCATAAAGATATTGGCACCCTTTATTTAGTATTTGGTGCTTGAGCCGGGATAGTTGGCACTGCATTAAGCCTTCTAATCCGAGCAGAATTAAGCCAACCAGGAGCCCTACTAGGGGATGATCAAATCTATAATGTTATTGTAACAGCACACGCATTTGTAATAATTTTTTTTATAGTAATACCTGTA",
    },
    {
        "species": "Lithobates catesbeianus",
        "common_name": "American Bullfrog",
        "group": "Amphibians",
        "gene": "COI",
        "accession": "PV085099.1",
        "sequence": "AAAGATATTGGAACCCTGTACTTAGTCTTCGGTGCCTGAGCCGGGATAGTCGGAACAGCCCTAAGTCTGCTGATTCGCGCAGAACTAAGCCAGCCAGGAACCCTCCTTGGCGACGATCAAATCTACAATGTTATCGTTACTGCTCACGCATTTGTTATAATTTTCTTCATAGTTATGCCTATCCTAATTGGAGGCTTTGG",
    },

]


# Load the database into a custom HashMap for storage and lookup.
# The HashMap maps species name -> sequence entry dict.
from data_structures.hash_map import HashMap

_database = HashMap()
for _entry in COI_DATABASE:
    _database.put(_entry["species"], _entry)


def get_all_sequences():
    """Return all COI barcode sequences from the HashMap."""
    return _database.values()


def get_sequence_by_species(species_name):
    """Look up a single species entry by scientific name using the HashMap."""
    return _database.get(species_name)


def get_species_list():
    """Return a list of all species names (keys) from the HashMap."""
    return _database.keys()
