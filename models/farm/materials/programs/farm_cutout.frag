#version 120
uniform sampler2D leafTexture;
uniform float removeWhiteBackground;
varying vec2 foliageUV;
varying float foliageLight;
void main()
{
    vec4 texel = texture2D(leafTexture, foliageUV);
    if (texel.a < 0.45) discard;
    float lowChannel = min(texel.r, min(texel.g, texel.b));
    float highChannel = max(texel.r, max(texel.g, texel.b));
    // Legacy plant JPEGs have a white background and no alpha channel.
    if (removeWhiteBackground > 0.5 && lowChannel > 0.78 && highChannel-lowChannel < 0.16) discard;
    gl_FragColor = vec4(texel.rgb * foliageLight, 1.0);
}
