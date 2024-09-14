"""
GroundT: Confirmed interactions in miR-Tarbase 6.1, Tarbase 7.0, and miRWalk 2.0

Description:
    This file contains a dictionary with experimentally confirmed miRNA-mRNA interactions
    from the databases mentioned above.

Format:
    A dictionary where each key is the name of an mRNA and each value is a list of miRNAs
    whose interactions with the mRNA can be found in at least one of the databases mentioned.

Example:
    GroundT = {
        "mRNA1": ["miRNA1", "miRNA2", "miRNA3"],
        "mRNA2": ["miRNA1", "miRNA4"],
        ...
    }

References:
    Chou, C.-H.; Chang, N.-W.; Shrestha, S.; et al. miRTarBase 2016: updates to the experimentally
    validated miRNA-target interactions database. Nucleic acids research, Oxford University Press,
    2015, 44, D239-D247.

    Vlachos, I. S.; Paraskevopoulou, M. D.; et al. DIANA-TarBase v7.0: indexing more than half
    a million experimentally supported miRNA: mRNA interactions. Nucleic acids research, Oxford 
    University Press, 2014, 43, D153-D159.

    Dweep, H.and Gretz, N. miRWalk2.0: a comprehensive atlas of microRNA-target interactions.
    Nature methods, Nature Publishing Group, 2015, 12, 697.
"""

# # Ejemplo de cómo se podría definir el dataset GroundT en Python
# GroundT = {
#     "VIM": ["miR-200b", "miR-200c", "miR-141"],
#     "ONECUT2": ["miR-9", "miR-124", "miR-29a"],
#     # Agrega más mRNAs y sus correspondientes miRNAs aquí
# }
