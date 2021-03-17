const Users={
'Пользователь':[
['Андрей','qwerty']
],
'Пользователь два':[
['Леонид','qwerty']
]
}
document.querySelector('.content').innerHTML=`<table class='users'></table>`
for(key in Users){
	let row = document.createElement('tr')
	row.innerHTML = `<td colspan=2>${key}</td>`
	document.querySelector('.users').appendChild(row)
for(let i=0;i<Users[key].length;i++){
let row =document.createElement('tr')
row.innerHTML = `
<td>${Users[key][i][0]}</td>
<td>${Users[key][i][1]}</td>
`
document.querySelector('.users').appendChild(row)}
}