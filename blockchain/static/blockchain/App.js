

function loadWeb3() {
    if (window.ethereum) {
      window.web3 = new Web3(window.ethereum)
      window.ethereum.enable()
      console.log("Web3 library is detected1")

    }
    else if (window.web3) {
      window.web3 = new Web3(window.web3.currentProvider)
      console.log("Web3 library is detected2")
    }
    else {
      console.log("No Web3 library detected")
    }
  }