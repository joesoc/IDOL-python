# IDOL-python
Python scripts to do various things with IDOL

##Category_get_hierarchyDetails.py
This script makes an ACI call to IDOL to get categories details.

The following is a an xml output of the script. 
```xml
<autnresponse xmlns:ns0="http://schemas.autonomy.com/aci/">
  <action>CATEGORYGETHIERDETAILS</action>
  <response>SUCCESS</response>
  <responsedata>
    <ns0:category>
      <ns0:numchildren>1</ns0:numchildren>
      <ns0:id>1</ns0:id>
      <ns0:name>AntiCorruption</ns0:name>
      <ns0:active>true</ns0:active>
      <ns0:location>
        <ns0:node>
          <ns0:id>0</ns0:id>
          <ns0:name>root category</ns0:name>
        </ns0:node>
      </ns0:location>
      <ns0:children>
        <ns0:child>
          <ns0:childid>277170445558660531</ns0:childid>
          <ns0:childname>IBAC</ns0:childname>
          <ns0:active>true</ns0:active>
          <ns0:numchildren>0</ns0:numchildren>
        </ns0:child>
      </ns0:children>
    </ns0:category>
  </responsedata>
</autnresponse>
```
