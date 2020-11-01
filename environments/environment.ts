# set up environment variables

export const environment = {
	production: false,
	apiServerUrl: 'http://127.0.0.1:5000/',
	auth0: {
		domain: 'fsnd79',
		audience: 'casting',
		clientId: 'tQtZK49lU42FD6sRTFFnxOvn7BpvINAi',
		callbackURL: 'http://localhost:5000/post-login'
		clientSecret: 'E5ptdSiVRlPluuhWFfDfnRKAgHQchRCHU9AXuVfq75iDD45NuQFXob3DwZmkqG0x'
	}

}