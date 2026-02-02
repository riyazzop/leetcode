type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | JSONValue[]

function isEmpty(obj: Obj): boolean {
    if(typeof obj===null)return true
    if(Array.isArray(obj))return obj.length===0
    if(typeof obj==='object')return Object.keys(obj).length===0
};