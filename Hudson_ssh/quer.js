var min_sourceid = "52011";
var max_sourceid = "55000";
var sourceid = "";
var url = "http://192.168.30.40:8080/gadgets/makeRequest";
var request_body = "";

for (sourceid = min_sourceid; sourceid<=max_sourceid; sourceid++)
{

try {
    xml_http = new ActiveXObject("MSXML2.ServerXMLHTTP");
}
catch (e) {
    WScript.StdOut.WriteLine("[-] XMLHTTP " + new Number(e.number).toHex() +
        ": Cannot create Active-X object (" + e.description) + ").";
    WScript.Quit(1);
}

try {
    xml_http.open("POST", url, false);
} catch (e) {
    WScript.StdOut.WriteLine("XMLHTTP Error");
    WScript.Quit(1);
}

var response_body = null;
var size_description = "?";
var file_size;


try {
    xml_http.setRequestHeader("Host", "192.168.30.40:8080");
    xml_http.setRequestHeader("Connection", "keep-alive");
    xml_http.setRequestHeader("Content-Length", "467");
    xml_http.setRequestHeader("Origin", "http://192.168.30.40:8080");
    xml_http.setRequestHeader("User-Agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1");
    xml_http.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xml_http.setRequestHeader("Accept", "*/*");
    xml_http.setRequestHeader("Referer", "http://192.168.30.40:8080/gadgets/ifr?container=default&mid=0&nocache=1&country=ALL&lang=ALL&view=default&parent=http%3A%2F%2F192.168.30.40%3A8080%2Findex.jsp%3A%2F%2F192.168.30.40%3A8080&st=canonical%3Ajohn.doe%3A4930%3Ashindig%3Ahttp%253A//localhost%253A8080/gwtgadget2/GwtGadget2.gadget.xml%3A0%3Adefault&url=http%3A%2F%2F192.168.30.40%3A8080%2Fgadgets%2FTable_jar.1120565708122%2FTable.gadget.xml");
    xml_http.setRequestHeader("Accept-Encoding", "gzip,deflate,sdch")
    xml_http.setRequestHeader("Accept-Language", "ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4");
    xml_http.setRequestHeader("Accept-Charset", "windows-1251,utf-8;q=0.7,*;q=0.3");
	request_body = ("url=http%3A%2F%2Flocalhost%3A8080%2Fresteasy%2Fws%2F64%2F") + sourceid + ("&httpMethod=POST&headers=Content-Type%3Dapplication%252Fx-www-form-urlencoded%253Bcharset%253DUTF-8&postData=autoNumber%3D") + sourceid + ("%26autoType%3D") + sourceid + ("%26time%3D25619804&authz=&st=&contentType=JSON&numEntries=3&getSummaries=false&signOwner=true&signViewer=true&gadget=http%3A%2F%2F192.168.30.40%3A8080%2Fgadgets%2FTable_jar.1120565708122%2FTable.gadget.xml&container=default&bypassSpecCache=1&getFullHeaders=false");
    xml_http.send (request_body);
    if (xml_http.status != 200) {
        WScript.StdOut.WriteLine("[-] HTTP " + xml_http.status + " " +
          xml_http.statusText);
        WScript.Quit(1);
    }
    response_body = xml_http.responseBody;
    size_description = xml_http.getResponseHeader("Content-Length");
        }

 

catch (e) {
    WScript.StdOut.WriteLine("XMLHTTP Error");
    WScript.Quit(1);
}

WScript.StdOut.WriteLine(xml_http.responseText);

}