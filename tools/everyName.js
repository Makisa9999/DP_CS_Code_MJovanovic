function everyName (a) {
    for (name in a) {
        console.log('Hello ' + a[name] + ' Welcome to the pary')
    }
    return 'Done'
}

console.log(everyName(['Joe','Mark','Carl','Wiliam']))