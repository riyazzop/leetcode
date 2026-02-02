type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): JSONValue[][] {
    const res:JSONValue[][]=[]
    let cur:JSONValue[]=[]
    for(let ele of arr){
        cur.push(ele)
        if(cur.length===size){
            res.push(cur)
            cur=[]
        }
    }
    if(cur.length>0)res.push(cur)
    return res
};
