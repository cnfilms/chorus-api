from chorusapi.constants.etat_courant_flux import EtatCourantFlux
from tabulate import tabulate

table_data = [[key, value.code, value.description]
              for key, value
              in EtatCourantFlux.__dict__.items()
              if not str(key).startswith('__')]

table = tabulate(table_data, headers=["Key", "code", "description"], tablefmt="rounded_outline")
print(table)
