// Import a Library to help create a component 
import React from 'react';
import { AppRegistry, View } from 'react-native';
import Header from './src/components/header';
import AlbumList from './src/components/AlbumList'; 

// Create a component. A component is some bit of jsx that is turned into react native
const App = () => (
	<View>
		<Header headerText={'Albums!'} />
		<AlbumList />
	</View>
);	


//Render to device using react-native run-android}

AppRegistry.registerComponent('albums', () => App);
