#!/usr/bin/env node

// Trial division

var primes = function(n) {
	var m = 4;
	for (m = 4 ; m < n; m++) {
		if (n % m == 0) { return 0;}
	};
	return n;
};
	

//Find first k primes

var firstkprimes = function(k) {
	var y = 1;
	var arr = [];
	for (y = 1; y < k+1; y++) {
		arr.push(primes(y));
	}
	return arr;
};

//Print to console

var fmt = function(arr) {
	return arr.join(",");
};

var k = 100;
console.log("firstkprimes(" + k + ")");
console.log(fmt(firstkprimes(k)));
