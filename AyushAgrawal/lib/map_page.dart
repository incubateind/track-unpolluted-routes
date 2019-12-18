
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:geolocator/geolocator.dart';



class MapPage extends StatefulWidget {
  @override
  _MapPageState createState() => _MapPageState();
}

class _MapPageState extends State<MapPage> {
  double lat = 0;
  double lon = 0;
getPos() async{
Position position = await Geolocator().getCurrentPosition(desiredAccuracy: LocationAccuracy.low);
setState(() {
  lat = position.latitude;
    lon = position.longitude;
});
print(lat);
print(lon);
}

@override
  void initState() {
    // TODO: implement initState
    super.initState();
  }


//   var src;
//   Future getDate() async{

//     var response = await http.get(Uri.encodeFull("https://1.base.maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/13/4400/2686/256/png8?apikey=wQr31osP43498vvxZLKv9TD8FLzm-UW4mCj5pa6LHRs"));
// print(response.body);
// setState(() {
  
//   src= response.body;
//   // final dejson = 
// });

//   }

  @override
  Widget build(BuildContext context) {
  
        return Scaffold(
          body: Container(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: <Widget>[
                Center(
                  child: RaisedButton(
                    child: Text("press"),
                    onPressed: (){
                    //  Navigator.of(context).push(MaterialPageRoute(
      // builder: (context) => DirectionPage()));
                    },
                  ),
                ),
                Container(
                  child: Image.network("https://1.base.maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/13/4400/2686/256/png8?apikey=wQr31osP43498vvxZLKv9TD8FLzm-UW4mCj5pa6LHRs")
                )

          ],
        ),
      ),
    );
  }
}