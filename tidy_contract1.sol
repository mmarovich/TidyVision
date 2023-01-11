// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

import "./Family.sol";

contract TidyVision is Family {

    mapping(address => uint) balances;

    function balance() public view returns(uint) {
        return balances[msg.sender];
    }
    function transferOwnership(address newParent, address newChild) external onlyOwner {
        parent = newParent;
        child = newChild;
    }

    //function addFunds(address payable _child) external payable onlyOwner {
    //    child = _child;
    //}


    function transfer(address payable recipient, uint value) public {
        require(msg.sender==parent && recipient==child, "You are not the parties in the contract, you cannot do the transfer!");
        // @TODO: replace the following with the .sub function
        balances[msg.sender] = balances[msg.sender] - value;
        // @TODO: replace the following with the .add function
        balances[recipient] = balances[recipient] + value;
    }

    function mint(address recipient, uint value) public {
        require(msg.sender == parent, "You do not have permission to mint tokens!");
        // @TODO: replace the following with the .add function
        balances[recipient] = balances[recipient] + value;
    }

    //function withdraw() external onlyFamily {
    //    payable(msg.sender).transfer(1000000000000000); // set to .001 ETH
        
    //}
}
