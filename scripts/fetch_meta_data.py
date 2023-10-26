from facebook_business.api import FacebookAdsApi
import pandas as pd

def fetch_meta_data():
    # Autenticação interativa
    my_app_id = input("Por favor, insira o seu App ID: ")
    my_app_secret = input("Por favor, insira o seu App Secret: ")
    my_access_token = input("Por favor, insira o seu Access Token: ")

    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

    # Puxar dados (este é um exemplo muito básico)
    from facebook_business.adobjects.adaccount import AdAccount
    from facebook_business.adobjects.campaign import Campaign

    ad_account_id = 'act_XXXXXXX'  # Substitua pelo seu Ad Account ID
    fields = [Campaign.Field.id, Campaign.Field.name]
    params = {
        'date_preset': 'last_7d',
    }

    ad_account = AdAccount(ad_account_id)
    campaigns = ad_account.get_campaigns(fields=fields, params=params)

    # Convertendo para DataFrame (para fins de exemplo)
    meta_data = []
    for campaign in campaigns:
        meta_data.append({
            'id': campaign[Campaign.Field.id],
            'name': campaign[Campaign.Field.name],
        })

    df = pd.DataFrame(meta_data)
    df.to_csv('../data/raw_meta_data.csv', index=False)

if __name__ == "__main__":
    fetch_meta_data()
