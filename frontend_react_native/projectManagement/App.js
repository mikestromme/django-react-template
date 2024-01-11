import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Home from './Screens/Home';
import {Contants} from 'expo-constants';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Hello There!!!</Text>      
     { <StatusBar style ="auto" />}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    //marginTop:Contants.statusBarHeight,
        
  },
});
