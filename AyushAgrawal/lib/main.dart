import 'package:carbon_trace/direction_page.dart';
import 'package:carbon_trace/map_page.dart';
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Carbon Trace',
      theme: ThemeData(
  
        primarySwatch: Colors.blue,
      ),
      home: MapPage(),
    );
  }
}
