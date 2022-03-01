#!/usr/bin/node

// Return reversed version of list
exports.esrever = function (list) {
	const rev = list.reduceRight((a, c) => (a.push(c), a), []);
	return rev;
};
