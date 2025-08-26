async function sha256(data) {
    const arrayData = new TextEncoder().encode(data)
    const hashBuffer = await window.crypto.subtle.digest("SHA-256", arrayData)
    return new TextDecoder().decode(hashBuffer)
    
}