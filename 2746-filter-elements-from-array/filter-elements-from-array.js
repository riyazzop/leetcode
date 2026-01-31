/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const newArr=[]
    arr.forEach((ele,i)=>{
        if(fn(ele,i))newArr.push(ele)
    })
    return newArr
};