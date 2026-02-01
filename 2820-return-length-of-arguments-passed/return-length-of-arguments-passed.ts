type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
    let res=0
    for(let arg in args){
        res+=1
    }
    return res
};

/**
 * argumentsLength(1, 2, 3); // 3
 */