import pandas as pd
from simple_salesforce import Salesforce

def salesforce_table_selectedColumns(username, password, token_number, table_name, fields, where_arg=None):
    sf = Salesforce(username=username, password=password, security_token=token_number)
    print('reading', table_name)

    fields = ',\n'.join(fields)
    sql = f"SELECT \n{fields} \nFROM {table_name} \n{where_arg}"
    sf_data = sf.query_all(sql)  # Json format
    output_df = pd.DataFrame(sf_data['records']).drop(columns='attributes')  # Convert to dataframe
    return output_df

def salesforce_table(table_name, username, password, token_number, where_arg=None):
    sf = Salesforce(username=username, password=password, security_token=token_number)
    print('reading', table_name)

    fields = [field.get('name') for field in getattr(sf, table_name).describe().get('fields')]
    fields = ',\n'.join(fields)
    sql = f"SELECT \n{fields} \nFROM {table_name} \n{where_arg}"
    sf_data = sf.query_all(sql)  # Json format
    output_df = pd.DataFrame(sf_data['records']).drop(columns='attributes')  # Convert to dataframe
    return output_df
