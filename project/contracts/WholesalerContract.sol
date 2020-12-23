pragma solidity >=0.5.1;

contract WholesalerContract{
     struct Product{
        string commonName;
        string country;
        uint16 quantity;
        string company;
        string executor;
        uint256 datetime;
    }
    
    mapping (address => uint16) public addressToProductId;
    mapping(uint16 => Product) public products;
  
    address[] public detailerssAccts;
    
    function addLink(uint16 _prodId, string memory _commonName,string memory _country, uint16 _quantity,string memory _company, string memory _executor) public {
        Product memory product = Product(_commonName, _country, _quantity,_company,_executor,block.timestamp);
        address _address = msg.sender;
        addressToProductId[_address] = _prodId;
        products[_prodId] = product;
    
        detailerssAccts.push(_address);
    }
    function getTransactionByProdId(uint16 _prodId) public view returns(uint16,string memory,string memory, uint16,string memory, string memory, uint256) {
        Product memory p = products[_prodId];
        return (_prodId,
        p.commonName, 
        p.country,
        p.quantity,
        p.company,
        p.executor,
        p.datetime);
    }
}