#version 120
varying vec2 foliageUV;
varying float foliageLight;
void main()
{
    gl_Position = ftransform();
    foliageUV = gl_MultiTexCoord0.xy;
    vec3 n = normalize(gl_Normal);
    foliageLight = 0.58 + 0.38 * abs(dot(n, normalize(vec3(0.4, -0.3, 0.85))));
}
