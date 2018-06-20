class primeFactors {
    for(i) {
        for (p of this.sieve(i)) {
        }
    }

    divmod(i, d) {
        q = Math.floor(i / d);
        r = i % d;
    }

    sieve(limit) {
        var nums = [...Array(limit + 1).keys()];
        nums[1] = 0;
        for (var i in nums) {
            if (i != 0) {
                console.log(limit, i);
                // for (var y = Math.pow(i, 2); y < limit; y += parseInt(i)) {
                //     console.log(y);
                //     nums[y] = 0;
                // }
            }
        }
        console.log(nums);

        // nums[1] = 0
        // for i in nums:
        //     if i:
        //         for y in range(i ** 2, limit, i):
        //             nums[y] = 0
        // return [i for i in nums if i > 0]
    }
}

if (require.main === module) {
    p = new primeFactors();
    p.sieve(100);
}
module.exports = primeFactors;
