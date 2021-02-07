function everyName (a) {
    for (name in a) {
        console.log('Welcome' + a[name] + '!')
    }
    return 'Done'
}

console.log(everyName(['Joe','Mark','Carl','Wiliam']))