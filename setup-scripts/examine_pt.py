import torch

file_path = "/home/b5cc/sanjukta.b5cc/metabolic_c1/datasets/ESM2_pert_features.pt"

try:
    data = torch.load(file_path)
    print(f"Data type: {type(data)}")
    print("Content:")
    print(data)
    
    # If it's a tensor, print shape
    if isinstance(data, torch.Tensor):
        print(f"Shape: {data.shape}")
        
    # If it's a dict, print keys
    elif isinstance(data, dict):
        print(f"Keys: {data.keys()}")
        
except Exception as e:
    print(f"Error loading file: {e}")


#gene_list = ["CHD4", "FOXC1", "SOX6", "TRIM5", "ZBTB20"]
gene_list = ['NC', 'FOXP1', 'RBAK', 'HAND2', 'ZNF331', 'DEDD2', 'TFEB', 'PLAGL1', 'NCOR2', 'FOS', 'HIF3A', 'IRF4', 'KLF4', 'TFAP2A', 'KLF7', 'BRCA1', 'DEK', 'TEAD1', 'SSB', 'KLF16', 'HIF1A', 'TRRAP', 'NR4A2', 'NMI', 'PPARA', 'PDLIM4', 'PBX3', 'FOXP2', 'SMAD2', 'EBF2', 'BDP1', 'BTG2', 'EP400', 'ZNF334', 'SMARCA4', 'FLI1', 'ZHX3', 'ZNF354B', 'NFIB', 'ZNF419', 'CHAF1A', 'ZFY', 'HMBOX1', 'NHLH1', 'ZNF26', 'ZNF44', 'DDX5', 'ZNF141', 'RORA', 'MXD1', 'TCEAL1', 'RXRG', 'KLF15', 'HMGA1', 'NAB1', 'RUNX1', 'CBFB', 'TWIST2', 'ABT1', 'HAX1', 'EDF1', 'TWIST1', 'NKX3-1', 'PWP1', 'MBD3', 'TSHZ2', 'AFF1', 'SOX13', 'PDCD11', 'ETV1', 'CREG1', 'PIAS4', 'TCERG1', 'RREB1', 'POLR2B', 'AATF', 'ZFPM2', 'TSC22D1', 'BCL6', 'ZNF254', 'KLF5', 'ZNF215', 'ANKRA2', 'NRIP1', 'ZNF146', 'GRB14', 'JARID2', 'HDAC2', 'SUPT5H', 'FASN', 'CEBPA', 'PPARD', 'PHF3', 'TRPS1', 'RB1', 'PLIN1', 'NR3C1', 'HMGN3', 'NPM1', 'RBBP7', 'ZFP2', 'REXO4', 'PBX1', 'EWSR1', 'EEF1A1', 'ZNF138', 'RNASEH2C', 'MEIS2', 'ZNF480', 'CIC', 'NFIA', 'TCF7L2', 'TCFL5', 'MEF2A', 'BTAF1', 'ZNF283', 'CNOT8', 'FAM136A', 'CEBPB', 'EP300', 'NFE2L1', 'TMEM107', 'SRPK1']

if isinstance(data, dict):
    missing_genes = [gene for gene in gene_list if gene not in data.keys()]
    if not missing_genes:
        print("All genes are present in the keys of the PT file.")
    else:
        print(f"The following genes are missing from the PT file: {missing_genes}")
else:
    print("The loaded data is not a dictionary; cannot check keys for genes.")