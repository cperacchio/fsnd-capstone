# set up environment variables

export const environment = {
	production: false,
	apiServerUrl: 'http://127.0.0.1:5000/',
	auth0: {
		domain: 'fsnd79',
		audience: 'casting',
		clientId: '2FaJjQSAtsiLqHMEfNlS0ThYQ6Oyuh9c',
		callbackURL: 'http://localhost:5000/post-login'
		clientSecret: 'zyo8mHSRsJPhveP8t0k3ZhdapaQs5Dcl-uZBoy6fJGjnTK8jM5lq5ySIDbSC7wVo'
	}

}