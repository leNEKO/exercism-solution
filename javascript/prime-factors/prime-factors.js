// Ah, ok, "for" needs to be a static method, my bad ...
class primeFactors {
    static for(limit) {
        var primes = [];
        var i = 2;
        while (limit >= i) {
            while (limit % i === 0) {
                primes.push(i);
                limit /= i;
            }
            i++;
        }
        return primes;
    }
}

module.exports = primeFactors;
