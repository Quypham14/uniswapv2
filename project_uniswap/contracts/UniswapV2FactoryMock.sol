// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '../node_modules/@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol';

contract UniswapV2FactoryMock {
    IUniswapV2Factory public uniswapV2Factory;

    constructor(address _uniswapV2Factory) {
        uniswapV2Factory = IUniswapV2Factory(_uniswapV2Factory);
    }

    function createPair(address tokenA, address tokenB) external returns (address) {
        return uniswapV2Factory.createPair(tokenA, tokenB);
    }
}
