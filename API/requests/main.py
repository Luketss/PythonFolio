#Local
import csv
import os
import json
#
import requests
import conns

SMARTTINVEST_NAME = "smarttinvest"
SMARTTINVEST_SHORTENING = "si"

FIELD_NAME = ["plano", "data"]

class Plano:

    def __init__(self, valor):
        self.code = valor.get('code'):
        self.createdAt = valor.get('createdAt')
        self.extra_data = valor.get('extra_data')
        self.interval = valor.get('interval')
        self.max_installments = valor.get('max_installments')
        self.name = valor.get('name')
        self.type = valor.get('type')
        self.value_cents = valor.get('value_cents')
        self.ano = valor.get('createdAt')

    def is_si_plan(self):
        splited_code = self.code.split("_")
        if SMARTTINVEST_NAME in splited_code or SMARTTINVEST_SHORTENING in splited_code:
        return True
    
    return False


def create_row_from_plan():
    return {
        "Planos": plan["code"],
        "data": plan[createdAt][0:10].replace("-","/")
    }


def write_files(plans):
    arv2016 = open("2016.csv", "a")
    arv2017 = open("2017.csv", "a")
    arv2018 = open("2018.csv", "a")
    arv2019 = open("2019.csv", "a")
    arv2020 = open("2020.csv", "a")


    writer_2016 = csv.DictWriter(arv2016, fieldnames=FIELD_NAME)
    writer_2017 = csv.DictWriter(arv2017, fieldnames=FIELD_NAME)
    writer_2018 = csv.DictWriter(arv2018, fieldnames=FIELD_NAME)
    writer_2019 = csv.DictWriter(arv2019, fieldnames=FIELD_NAME)
    writer_2020 = csv.DictWriter(arv2020, fieldnames=FIELD_NAME)


    writer_2016.writeheader()
    writer_2017.writeheader()
    writer_2018.writeheader()
    writer_2019.writeheader()
    writer_2020.writeheader()


    #dictionary.get(keyname, value) > The keyname of the item you want to return the value from. Value is optional, return value if keyname not 
    for plan in plans:
        year = plan["createdAt"][0:4]
        row = create_row_from_plan(plan)

        if(year == "2016"):
            #write all plans created at 2016
            writer_2016.writerow(row)

        if(year == "2017"):
            #write all plans created at 2017
            awriter_2017.writerow(row)

        if(year == "2018"):
            #write all plans created at 2018
            writer_2018.writerow(row)

        if(year == "2019"):
            #write all plans created at 2019
            writer_2019.writerow(row)

        if(year == "2020"):
            #write all plans created at 2020
            writer_2020.writerow(row)


    close_files(arv2016, arv2017, arv2018, arv2019, arv2020)


def close_files(*args):
    for file in args:
        file.close()


def write_csv_in_batch(plans, file_name):
    with open(file_name, "w") as csv_file:
        writer = csv.DictWriter(csv_file, FIELD_NAME)
        writer.writeheader()

        dict_plans = [create_row_from_plan(plan) for plan in plans]

        writer.writerows(dict_plans)


def separate_si_sb(plans):
    si = []
    sb = []

    for plan in plans:	    
        if Plano.is_si_plan(plan):
            si.append(plan)
        else:
            sb.append(plan)
  
 
    write_csv_in_batch(si, "si_plans.csv")
    write_csv_in_batch(sb, "sb_plans.csv")


if __name__ == "__main__":
    url = conns.connect.getenv()
    plans = conns.connect.get_plans(url)   
    write_files(plans)
    separate_si_sb(plans)
    #fndfjhsdbfvk shfbsdhv bv sdfvsbdcvnsdf s
