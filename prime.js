#!/usr/bin/env node

// Trial division
// https://en.wikipedia.org/wiki/Trial_division

var primes = function(n) {
	var m = 1;
	for (m = 2 ; m < n; m++) {
		if (n === 2 || n === 3) { return n;}
		else if (n % m == 0) { return null;}
	};
	return n;
};
	
//Find first k primes

var firstkprimes = function(k) {
	var y = 2;
	var arr = [];
	for (y = 2; y < k+1; y++) {
		if (primes(y) != null) {arr.push(primes(y));}
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

// Check? Is this right?
// https://en.wikipedia.org/wiki/Prime_number#Definition_and_examples

var check = function() {
	var realPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	var rPstring = realPrimes.toString();
	var fkPstring = firstkprimes(100).toString();
	if (rPstring == fkPstring) { return console.log("...as found on Wiki.");}
	else { return "These aren't actually primes.";}
};

check()
