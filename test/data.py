import os
from pyensembl import Locus, Genome

def data_path(name):
    """
    Return the absolute path to a file in the test/data directory.
    The name specified should be relative to test/data.
    """
    return os.path.join(os.path.dirname(__file__), "data", name)

# mapping of ensembl releases to transcript IDs for FOXP3-001
FOXP3_001_transcript_id = "ENST00000376207"

TP53_gene_id = "ENSG00000141510"

# beta-catenin interacting protein from the negative strand of chromosome 1
# URL: http://useast.ensembl.org/Homo_sapiens/Transcript/Sequence_cDNA?
#      db=core;g=ENSG00000178585;r=1:9848276-9910336;t=ENST00000377256
CTNNBIP1_004_transcript_id = "ENST00000377256"

# coding sequence for beta-catenin interacting protein (CTNNBIP1-004)
CTNNBIP1_004_CDS = "".join([
    "ATG",
    "AACCGCGAGGGAGCTCCCGGGAAGAGTCCGGAG",
    "GAGATGTACATTCAGCAGAAGGTCCGAGTGCTGCTCATGCTGCGGAAGATGGGATCAAAC",
    "CTGACAGCCAGCGAGGAGGAGTTCCTGCGCACCTATGCAGGGGTGGTCAACAGCCAGCTC",
    "AGCCAGCTGCCTCCGCACTCCATCGACCAGG",
    "GTGCAGAGGACGTGGTGATGGCGTTTTCCAGGTCGGAGACGGAAGACCGGAGGCAG",
    "TAG"
])

# 5' UTR for beta-catenin interacting protein (CTNNBIP1-004)
CTNNBIP1_004_UTR5 = "".join([
    "TGTGGGTGCAGGTTTCCTGGGCTTGCCAGACACACAGGGCGGCACCTTCCTACTTCTGCC",
    "CAGCCACAGCCCTCCCCTCACAGTTGAGCACCTGTTTGCCTGAAGTTAATTTCCAGAAGC",
    "AGGAGTCCCCAGAGCCAGGCAGGGGG"])

# 3' UTR for beta-catenin interacting protein (CTNNBIP1-004)
CTNNBIP1_004_UTR3 = \
    "CTGCAAAGCCCTTGGAACACCCTGGATGCTGTTGAGGGCCAAGAGATCTGTGTGGCTCC"

CTNNBIP1_004_locus = Locus("1", 9850659, 9878176, "-")

# properties of CTNNBIP1-004's exons copied from
# http://useast.ensembl.org/Homo_sapiens/Transcript/Exons?g=ENSG00000178585;
# r=1:9850659-9878176;redirect=no;t=ENST00000377256
CTTNNIP1_004_exon_ids = [
    'ENSE00001473268',
    'ENSE00001643659',
    'ENSE00001600669',
    'ENSE00001267940',
    'ENSE00001473265',
]

CTTNNIP1_004_exon_lengths = [
    37,
    85,
    120,
    91,
    118
]


#
# Information for EGFR from Ensembl website
# Date: March 25th, 2015
# Ensembl Release: 79
#
EGFR_001_name = "EGFR-001"
EGFR_001_transcript_id = "ENST00000275493"
EGFR_001_ccds_id = "CCDS5514"
EGFR_001_protein_id = "ENSP00000275493"
EGFR_001_protein_sequence = "".join([
    "MRPSGTAGAALLALLAALCPASRALEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNNCEVVLGNLEITYV",
    "QRNYDLSFLKTIQEVAGYVLIALNTVERIPLENLQIIRGNMYYENSYALAVLSNYDANKTGLKELPMRNL",
    "QEILHGAVRFSNNPALCNVESIQWRDIVSSDFLSNMSMDFQNHLGSCQKCDPSCPNGSCWGAGEENCQKL",
    "TKIICAQQCSGRCRGKSPSDCCHNQCAAGCTGPRESDCLVCRKFRDEATCKDTCPPLMLYNPTTYQMDVN",
    "PEGKYSFGATCVKKCPRNYVVTDHGSCVRACGADSYEMEEDGVRKCKKCEGPCRKVCNGIGIGEFKDSLS",
    "INATNIKHFKNCTSISGDLHILPVAFRGDSFTHTPPLDPQELDILKTVKEITGFLLIQAWPENRTDLHAF",
    "ENLEIIRGRTKQHGQFSLAVVSLNITSLGLRSLKEISDGDVIISGNKNLCYANTINWKKLFGTSGQKTKI",
    "ISNRGENSCKATGQVCHALCSPEGCWGPEPRDCVSCRNVSRGRECVDKCNLLEGEPREFVENSECIQCHP",
    "ECLPQAMNITCTGRGPDNCIQCAHYIDGPHCVKTCPAGVMGENNTLVWKYADAGHVCHLCHPNCTYGCTG",
    "PGLEGCPTNGPKIPSIATGMVGALLLLLVVALGIGLFMRRRHIVRKRTLRRLLQERELVEPLTPSGEAPN",
    "QALLRILKETEFKKIKVLGSGAFGTVYKGLWIPEGEKVKIPVAIKELREATSPKANKEILDEAYVMASVD",
    "NPHVCRLLGICLTSTVQLITQLMPFGCLLDYVREHKDNIGSQYLLNWCVQIAKGMNYLEDRRLVHRDLAA",
    "RNVLVKTPQHVKITDFGLAKLLGAEEKEYHAEGGKVPIKWMALESILHRIYTHQSDVWSYGVTVWELMTF",
    "GSKPYDGIPASEISSILEKGERLPQPPICTIDVYMIMVKCWMIDADSRPKFRELIIEFSKMARDPQRYLV",
    "IQGDERMHLPSPTDSNFYRALMDEEDMDDVVDADEYLIPQQGFFSSPSTSRTPLLSSLSATSNNSTVACI",
    "DRNGLQSCPIKEDSFLQRYSSDPTGALTEDSIDDTFLPVPEYINQSVPKRPAGSVQNPVYHNQPLNPAPS"
    "RDPHYQDPHSTAVGNPEYLNTVQPTCVNSTFDSPAHWAQKGSHQISLDNPDYQQDFFPKEAKPNGIFKGS"
    "TAENAEYLRVAPQSSEFIGA"
])


# GTF cropped from ftp://ftp.ensembl.org/pub/release-81/gtf/mus_musculus/
# Mus_musculus.GRCm38.81.gtf.gz via:
# grep "ENSMUSG00000017167" Mus_musculus.GRCm38.81.gtf

# Transcript FASTA cropped from ftp://ftp.ensembl.org/pub/release-81/
# fasta/mus_musculus/cdna/Mus_musculus.GRCm38.cdna.all.fa.gz via:
# grep "ENSMUSG00000017167" Mus_musculus.GRCm38.cdna.all.fa -A 50

# ncRNA FASTA cropped from ftp://ftp.ensembl.org/pub/release-81/
# fasta/mus_musculus/cdna/Mus_musculus.GRCm38.ncrna.fa.gz via:
# grep "ENSMUSG00000088969" Mus_musculus.GRCm38.ncrna.fa -A 2

# Protein FASTA cropped from ftp://ftp.ensembl.org/pub/release-81/fasta/
# mus_musculus/pep/Mus_musculus.GRCm38.pep.all.fa.gz via:
# grep "ENSMUSG00000017167" Mus_musculus.GRCm38.pep.all.fa -A 50

# Tested against:
# http://useast.ensembl.org/Mus_musculus/Gene/Summary?db=core;g=ENSMUSG00000017167

MOUSE_ENSMUSG00000017167_PATH = data_path(
    "mouse.ensembl.81.partial.ENSMUSG00000017167.gtf")
MOUSE_ENSMUSG00000017167_TRANSCRIPT_FASTA_PATH = data_path(
    "mouse.ensembl.81.partial.ENSMUSG00000017167.fa")
MOUSE_ENSMUSG00000088969_NCRNA_FASTA_PATH = data_path(
    "mouse.ensembl.81.partial.ncrna.ENSMUSG00000017167.fa")
MOUSE_ENSMUSG00000017167_PROTEIN_FASTA_PATH = data_path(
    "mouse.ensembl.81.partial.ENSMUSG00000017167.pep")


custom_mouse_genome_grcm38_subset = Genome(
    reference_name="GRCm38",
    annotation_name="_test_mouse_ensembl81_subset",
    gtf_path_or_url=MOUSE_ENSMUSG00000017167_PATH,
    transcript_fasta_paths_or_urls=[MOUSE_ENSMUSG00000017167_TRANSCRIPT_FASTA_PATH],
    protein_fasta_paths_or_urls=[MOUSE_ENSMUSG00000017167_PROTEIN_FASTA_PATH])

def setup_init_custom_mouse_genome():
    """
    If a unit test needs to start from a cleared cache, add this to the test
    setup.
    """
    custom_mouse_genome_grcm38_subset.clear_cache()
    custom_mouse_genome_grcm38_subset.index()
