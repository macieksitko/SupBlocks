from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import sys
import os

links = ['producer','shipper','wholesaler','detailer']


current_acc = "0xc9CE6B1bE8B790952878bF0F6041b96057eb9d4E"
private_key_for_senders_account = os.getenv("INFURA_PRIV_KEY")
class TransactionService:
    
    def setup_blockchain_connection(self):
        global web3
        url = "HTTP://127.0.0.1:7545"
        web3 = Web3(Web3.WebsocketProvider('wss://rinkeby.infura.io/ws/v3/97a0faed640a4384b1a99d03e55e5f19'))
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        #web3 = Web3(Web3.HTTPProvider(url))
        #web3.eth.defaultAccount = current_acc
        
    def setup_contract(self,current_link):
        global current_user, contract,address
        current_user = current_link

        if current_user == "producer":
            with open("build/contracts/ProducerContract.json") as f:
                info_json = json.load(f)
            address = "0xEAA8e712605a6737D30E550055f495A76C233014"
        elif current_user == "shipper":
            with open("build/contracts/ShipperContract.json") as f:
                info_json = json.load(f)
            address = "0xeD8b9e7B7D615443b60cDD6746752e0BBbE78593"
        elif current_user == "wholesaler":
            with open("build/contracts/WholesalerContract.json") as f:
                info_json = json.load(f)
            address = "0x88bdcD736fd180C8CEfd8DC65E37dCab00F958a8"
        elif current_user == "detailer":
            with open("build/contracts/DetailerContract.json") as f:
                info_json = json.load(f)
            address = "0xC1Ba6143665D85066244cF11C91058b7Ab12e504"
        elif current_user == "user":
            with open("build/contracts/UserContract.json") as f:
                info_json = json.load(f)
            address = "0x450BcDf15bF4cBfdd13fECE8d3F8FaB8d8519c82"

        abi = info_json["abi"]
        contract = web3.eth.contract(abi = abi, address = address)
    def add_link(self,form):
        
        if current_user == "producer":
           
            nonce = web3.eth.getTransactionCount(current_acc)
            transaction = contract.functions.addLink(
                form.cleaned_data.get("product_id"),
                form.cleaned_data.get("common_name"),
                form.cleaned_data.get("expiry_date"),
                form.cleaned_data.get("country"),
                form.cleaned_data.get("quantity"),
                form.cleaned_data.get("company"),
                form.cleaned_data.get("executor")
                ).buildTransaction({
                'gas': 500000,
                'gasPrice': web3.toWei('21', 'gwei'),
                'from': current_acc,
                'nonce': nonce
            }) 

        elif current_user == "shipper":
            nonce = web3.eth.getTransactionCount(current_acc)
            transaction = contract.functions.addLink(
                form.cleaned_data.get("product_id"),
                form.cleaned_data.get("common_name"),
                form.cleaned_data.get("country"),
                form.cleaned_data.get("quantity"),
                form.cleaned_data.get("company"),
                form.cleaned_data.get("executor")
                ).buildTransaction({
                'gas': 500000,
                'gasPrice': web3.toWei('21', 'gwei'),
                'from': current_acc,
                'nonce': nonce
            }) 

        elif current_user == "wholesaler":
            nonce = web3.eth.getTransactionCount(current_acc)
            transaction = contract.functions.addLink(
                form.cleaned_data.get("product_id"),
                form.cleaned_data.get("common_name"),
                form.cleaned_data.get("country"),
                form.cleaned_data.get("quantity"),
                form.cleaned_data.get("company"),
                form.cleaned_data.get("executor")
                ).buildTransaction({
                'gas': 500000,
                'gasPrice': web3.toWei('21', 'gwei'),
                'from': current_acc,
                'nonce': nonce
            }) 

        elif current_user == "detailer":
            nonce = web3.eth.getTransactionCount(current_acc)
            transaction = contract.functions.addLink(
                form.cleaned_data.get("product_id"),
                form.cleaned_data.get("common_name"),
                form.cleaned_data.get("country"),
                form.cleaned_data.get("quantity"),
                form.cleaned_data.get("company")
                 ).buildTransaction({
                'gas': 500000,
                'gasPrice': web3.toWei('21', 'gwei'),
                'from': current_acc,
                'nonce': nonce
            }) 

        signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key_for_senders_account)
        web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    def get_link_by_id(self,id):
        return contract.functions.getTransactionByProdId(int(id)).call()

    def get_all_links(self,id):
        links_dict = {}
        self.setup_contract("user")

        links_dict["producer"] = contract.functions.getProducer(int(id)).call()
        print(links_dict["producer"])
        links_dict["shipper"] = contract.functions.getShipper(int(id)).call()
        links_dict["wholesaler"] = contract.functions.getWholesaler(int(id)).call()
        links_dict["detailer"] = contract.functions.getDetailer(int(id)).call()
        print(address)
        return links_dict
        

    
         