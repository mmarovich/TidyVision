// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

import "./Family.sol";

contract TidyVision is Family {
    
    receive() external payable {}

    function transferOwnership(address newParent, address newChild) external onlyOwner {
        parent = newParent;
        child = newChild;
    }

    function addFunds(address _child) external payable onlyOwner {
        child = _child;
    }

    function withdraw() external onlyFamily {
        payable(msg.sender).transfer(1000000000000000); // set to .001 ETH
        
    }
}
