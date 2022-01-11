# ##########
# import argparse
# import os
#
# parser = argparse.ArgumentParser()
# parser.add_argument("-f", "--file", type=str, help="nom du fichier à créer")
# parser.add_argument("-p", "--path", type=str, help="chemin vers le dossier à scanner")
# args = parser.parse_args()
#
# if args.path:
#     ls = os.listdir(args.path)
#     for i in ls:
#         print(i)
#
# if args.file:
#     with open(args.file, "x"):
#         print("le fichier {} a bien été créé".format(args.file))
#
# ##########
# import argparse
#
# crea = argparse.ArgumentParser()
# crea.add_argument("-n","--nom", type=argparse.FileType("w"), help="nom du fichier")
# args = crea.parse_args()
# ##########
import argparse
import os
nav = argparse.ArgumentParser()
nav.add_argument("-c","--cherche", type=str, help="affiche le fichier et le dossier d'un repertoire")