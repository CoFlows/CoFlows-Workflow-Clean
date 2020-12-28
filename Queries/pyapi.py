### <info version="1.0.100">
###     <title>Python Query Test API</title>
###     <description>Python Query API with samples for permissions, documentation and function definitions</description>
###     <termsOfService url="https://www.coflo.ws"/>
###     <contact name="Arturo Rodriguez" url="https://www.coflo.ws" email="arturo@coflo.ws"/>
###     <license name="Apache 2.0" url="https://www.apache.org/licenses/LICENSE-2.0.html"/>
### </info>

import QuantApp.Kernel as qak

### <api name="Add">
###     <description>Function that adds two numbers</description>
###     <returns>returns an integer</returns>
###     <param name="x" type="integer">First number to add</param>
###     <param name="y" type="integer">Second number to add</param>
###     <permissions>
###         <group id="9a7adf48-183f-4d44-8ab2-c0afd1610c71" permission="read"/>
###     </permissions>
### </api>
def Add(x, y):
    return x + y

import json
### <api name="Print">
###     <description>Function that prints a json</description>
###     <returns>returns an integer</returns>
###     <param name="x" type="string">JSON object</param>
###     <permissions>
###         <group id="9a7adf48-183f-4d44-8ab2-c0afd1610c71" permission="read"/>
###     </permissions>
### </api>
def Print(x):
    return json.loads(x)

import pandas as pd
### <api name="Panda">
###     <description>Function that uses a dataframe's group by</description>
###     <returns>returns an string</returns>
###     <param name="x" type="string">List of x values</param>
###     <param name="y" type="string">List of y values</param>
###     <permissions>
###         <group id="9a7adf48-183f-4d44-8ab2-c0afd1610c71" permission="read"/>
###     </permissions>
### </api>
def Panda(x, y):
    xlist = list(x.split(','))
    ylist = list(y.split(','))

    df = pd.DataFrame(list(zip(xlist, ylist)), columns =['X', 'Y']).groupby(['X']).count().rename(columns={ 'Y': 'count' })

    return df.to_string()

import pandas as pd
### <api name="Panda">
###     <description>Function that uses a dataframe's group by</description>
###     <returns>returns an string</returns>
###     <param name="x" type="string">List of x values</param>
###     <param name="y" type="string">List of y values</param>
###     <permissions>
###         <group id="9a7adf48-183f-4d44-8ab2-c0afd1610c71" permission="read"/>
###     </permissions>
### </api>
def Panda2(_table):
    table = json.loads(_table)
    
    df = pd.DataFrame(list(zip(table['x'], table['y'])), columns =['X', 'Y']).groupby(['X']).count().rename(columns={ 'Y': 'count' })

    return df.to_string()


### <api name="Permission">
###     <description>Function that returns a permission</description>
###     <returns> returns an string</returns>
###     <permissions>
###         <group id="9a7adf48-183f-4d44-8ab2-c0afd1610c71" permission="view"/>
###     </permissions>
### </api>
def Permission():
    quser = qak.User.ContextUser
    permission = qak.User.PermissionContext("9a7adf48-183f-4d44-8ab2-c0afd1610c71")
    if permission == qak.AccessType.Write:
        return quser.FirstName + " WRITE"
    elif permission == qak.AccessType.Read:
        return quser.FirstName + " READ"
    elif permission == qak.AccessType.View:
        return quser.FirstName + " VIEW"
    else:
        return quser.FirstName + " DENIED"