import * as React from 'react';
import { Text, View, StyleSheet, TouchableOpacity,Image ,SafeAreaView} from 'react-native';
import Constants from 'expo-constants';


export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.appBar}>
        <Text style={styles.paragraph}>Chess Board</Text>
      </View>
      <View style={styles.board}>
        <Row1></Row1>
        <Row2></Row2>
        <Row1></Row1>
        <Row2></Row2>
        <Row1></Row1>
        <Row2></Row2>
        <Row1></Row1>
        <Row2></Row2>
      </View>
  <View  style={{flex:0.5}}></View>
     
    </SafeAreaView>
  );
}


const Row1 = (icon) => {
  return (
    <View style={{ flex: 1, flexDirection: 'row' }}>
      <TouchableOpacity style={{ backgroundColor: 'black', flex: 1 }}>
       
        <Text></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'white', flex: 1 }}>
        <Text style={{color:'white'}}></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'black', flex: 1 }}>
        <Text></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'white', flex: 1 }}>
        <Text ></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'black', flex: 1 }}>
        <Text></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'white', flex: 1 }}>
        <Text ></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'black', flex: 1 }}>
        <Text></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'white', flex: 1 }}>
        <Text > </Text>
      </TouchableOpacity>
    </View>
  );
};

const Row2 = () => {
  return (
    <View style={{ flex: 1, flexDirection: 'row' }}>
      <TouchableOpacity style={{ backgroundColor: 'white', flex: 1 }}>
        <Text ></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'black', flex: 1 }}>
        <Text ></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'white', flex: 1 }}>
        <Text ></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'black', flex: 1 }}>
        <Text ></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'white', flex: 1 }}>
        <Text ></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'black', flex: 1 }}>
        <Text></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'white', flex: 1 }}>
        <Text ></Text>
      </TouchableOpacity>
      <TouchableOpacity style={{ backgroundColor: 'black', flex: 1 }}>
        <Text></Text>
      </TouchableOpacity>
    </View>
  );
};


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    paddingTop: Constants.statusBarHeight,
    backgroundColor: 'tomato',
    padding: 8,
  },
  paragraph: {
    margin: 15,
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    color: 'white',
  },

  appBar:{
     flex: 0.5, backgroundColor: 'black',height:30 ,
    
  },
  board: {
    flex: 3,
    borderWidth: 5,
    borderColor:'yellow',
    marginTop:90,
  
    marginHorizontal:30,
    marginBottom: 50,
    
    
  },
});