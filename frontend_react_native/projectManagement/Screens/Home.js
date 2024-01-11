import React, { Component } from 'react'
import { StyleSheet, Text, View } from 'react-native';
import {Card} from 'react-native-paper';

export class Home extends Component {
  render() {
    return (
    <Card style={styles.cardStyle}>
      <Text>Hello from home!!!</Text>
    </Card>
    )
  }
} 

const styles = StyleSheet.create({
    cardStyle:{
        padding:10,
        margin:10
    }


})

export default Home