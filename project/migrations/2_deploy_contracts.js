const Producer = artifacts.require("ProducerContract");
const Shipper = artifacts.require("ShipperContract");
const Wholesaler = artifacts.require("WholesalerContract");
const Detailer = artifacts.require("DetailerContract");


module.exports = function (deployer) {
  deployer.deploy(Producer)
    .then(() => console.log(Producer.address));
  deployer.deploy(Shipper)
    .then(() => console.log(Shipper.address));
  deployer.deploy(Wholesaler)
    .then(() => console.log(Wholesaler.address));
  deployer.deploy(Detailer)
    .then(() => console.log(Detailer.address));
};