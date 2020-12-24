pragma solidity >=0.5.1;

import "./ProducerContract.sol";
import "./ShipperContract.sol";
import "./WholesalerContract.sol";
import "./DetailerContract.sol";

contract UserContract{
    

    function getProducer(uint16 _prodId) public view returns (uint16,string memory,string memory, string memory, uint16,string memory,string memory, uint256){
        address t = 0xEAA8e712605a6737D30E550055f495A76C233014;
        ProducerContract producer = ProducerContract(t);
        return producer.getTransactionByProdId(_prodId);
    }

    function getShipper(uint16 _prodId) public view returns (uint16,string memory,string memory, uint16,string memory,string memory, uint256){
        address _t = 0xeD8b9e7B7D615443b60cDD6746752e0BBbE78593;
        ShipperContract shipper = ShipperContract(_t);
        return shipper.getTransactionByProdId(_prodId);
    }

    function getWholesaler(uint16 _prodId) public view returns (uint16,string memory,string memory, uint16,string memory, string memory, uint256){
        address _t = 0x88bdcD736fd180C8CEfd8DC65E37dCab00F958a8;
        WholesalerContract wholesaler = WholesalerContract(_t);
        return wholesaler.getTransactionByProdId(_prodId);
    }

    function getDetailer(uint16 _prodId) public view returns (uint16,string memory,string memory, uint16,string memory, uint256){
        address _t = 0xC1Ba6143665D85066244cF11C91058b7Ab12e504;
        DetailerContract detailer = DetailerContract(_t);
        return detailer.getTransactionByProdId(_prodId);
    }

}